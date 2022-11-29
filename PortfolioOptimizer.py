import pandas as pd
import numpy as np
import scipy as sp

class PortfolioOptimizer:
    def __init__(self, asset_price_file_loc, rf=0.01):  # amikor elkészül az objektum, milyen lépések hajtódjanak végre
        #    pass #self: arra az egy darab pldányra vonatkozik, amit meghívtunk. Számontartja, mit tartalmaz a portf. opimizer
        self._asset_file_loc = asset_price_file_loc
        self._read_asset_file()  # '/content/drive/My Drive/numpu4/Price_history.csv'
        self._calc_asset_metrics()
        self._rf=rf

    #  def add_constraints(self,long_only=false):

    def _read_asset_file(self):
        price_hist_df = pd.read_csv(self._asset_file_loc, index_col=0)  # underscore: "ezzel nem érdemes foglalkozni"
        price_hist_df.columns = [colname.replace("_price", "") for colname in price_hist_df.columns]
        price_hist_df.index = pd.to_datetime(price_hist_df.index)
        price_hist_df.fillna(method='ffill')  # ffill = forward fill
        self._price_hist_df = price_hist_df

    def _calc_asset_metrics(self):
        self._return_asset = self._price_hist_df / self._price_hist_df.shift(1) - 1
        self._mean_asset = self._return_asset.mean() * 12  # évestett metrika
        self._std_asset = self._return_asset.std() * np.sqrt(12)  # évesített szórás
        self._cov_asset = self._return_asset.cov() * 12  # évesített
        self._corr_asset = self._return_asset.corr()

    # @staticmethod: osztályon belül logikailag oda tartozó, de azon nemoperál függvény: kiirtja a self-et "dekorátor"
    @staticmethod
    def _calc_nasset_std(w, cov_matrix):

        return np.sqrt(np.dot(np.dot(w, cov_matrix), w.transpose()))

    @staticmethod
    def _calc_nasset_mean(w, mean_return):

        return np.sum(w * mean_return)  # 2 vektor elemenkénti szorzata --> összeadjuk

    @staticmethod
    def calc_nasset_cov(w, cov_matrix):
        return np.sqrt(np.dot(np.dot(w, cov_matrix), w.transpose()))  # np.dot  mátrix szorzat

    def _calc_eff_frontier(self):
        eff_frontier = {}
        for return_target in np.linspace(0.01, 0.2, 100):
            # return_target = 0.2
            cons = (
            {'type': 'eq', 'fun': lambda weight: return_target - self.calc_nasset_mean(weight, self._mean_asset)},
            {'type': 'eq', 'fun': lambda weight: np.sum(weight) - 1},
            # {'type': 'ineq', 'fun':lambda weight: 0.8 - np.max(weight)}
            )
            bounds = []
            for i in range(self._mean_asset.shape[0]):
                bounds.append((0, None))
            res = sp.optimize.minimize(self.calc_nasset_cov, np.array([1, 0, 0, 0, 0]), args=(self._cov_asset),
                                       constraints=cons,
                                       bounds=bounds)  # a szórást akarjuk minimalizálni. Kezdőérték az [1,...] array
            # args: minden maradék argumentuma a függvénynek, ami mentén NEM optimalizálunk
            eredmeny = res.x
            if res.success:  # magától ellenőrzi, hogy true vagy false (==True)
                eff_frontier[return_target] = res.x

            eff_frontier_df = pd.DataFrame(eff_frontier).transpose()
            print(eff_frontier_df.head(20))
            # eff_frontier_df.apply(lambda x: calc_nasset_std(x, std_asset), axis=1) #vagy soronként vagy oszloponként meghívunk függvényt hozzá
            eff_frontier_df["Standard dev."] = eff_frontier_df.apply(lambda x: self._calc_nasset_std(np.array(x), self._cov_asset),
                                                                     axis=1)
            eff_frontier_df.reset_index(inplace=True)
            eff_frontier_df.plot(x="Standard dev.", y="index")

        return eff_frontier_df

    def _calc_spline_for_eff_frontier(self):
        eff_fr_points = self.calc_eff_frontier()
        index_to_filter=eff_fr_points["Standard dev."].argmin()
        eff_fr_points=eff_fr_points.loc[24:]
        cs = sp.interpolate.CubicSpline(eff_fr_points)

    def calcCAL(self):
        cs = self._calc_spline_for_eff_frontier()

        def system_of_equations(params):
            equation_1=params[0]-self._rf
            equation_2=params[1]-cs.deriv()
            equation_3=params[0]+params[1]*params[2]-cs(params[2])
            return[equation_1, equation_2, equation_3]
        CAL_params=sp.optimize.fsolve(func=system_of_equations(), x0=[self._rf, 0.2,0.2])
