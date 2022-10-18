import numpy as np

#function (r_exp, vols, numOfPath)
#numOfPath sora


def generated_uncorrelated_returns (expected_returns, vols, numOfPath):
    a_exp_rets=np.array(expected_returns)\
      -(np.array(vols)**2)/2

    numofassets=len(expected_returns)
    rets=np.random.normal(
        a_exp_rets, vols, (numOfPath, numofassets))
    #a= np.zeros((numofassets, numOfPath))
    #a = np.random.normal(rs, vols, size= (numofassets,numOfPath))
    return rets

def test_generated_uncorrelated_returns():
    rs1 = [0.1, 0.05]
    vols1 = [0.2, 0.1]
    numOfPath = 2000
    a_rets = (generated_uncorrelated_returns(rs1, vols1, numOfPath))
    print(a_rets.mean(axis=0))

rs1=[0.1, 0.05]
vols1=[0.2, 0.1]
numOfPath = 2000
a_rets=(generated_uncorrelated_returns(rs1, vols1, numOfPath))
print(a_rets.mean(axis=0))

def correlated_std_norm(corr_mat, numOfPath):
    a_corr = np.array(corr_mat)
    a_l = np.linalg.cholesky(a_corr)
    numofassets=a_l.shape[0]
    a_uncorr=np.random.normal(size=(numOfPath, numofassets))

    #check correlation structure
    print(np.corrcoef(a_uncorr.transpose))
    a_corr=np.dot(a_uncorr,a_l.transpose())
    return a_corr

def test_correlated_std_norm():
    corr_mat = [[1.0, -0.8], [-0.8, 1]]
    a_corr=correlated_std_norm(corr_mat, 10000)
    print(np.corrcoef(a_corr.transpose()))
    #print(np.dot(a_l*a_l.transpose()))

def correlated_norm(exp_values, stds, corr_mat, numOfPath):
    a_corr=correlated_std_norm(corr_mat, numOfPath)
    a_res=a_corr*np.array(stds)\
          +np.array(exp_values)
    return a_res
def test_correlated_norm():
    exp_values=[0.08,0.0495]
    stds=[0.2,0.1]
    corr_mat = [[1.0, -0.8], [-0.8, 1]]
    a_res=correlated_norm(exp_values, stds, corr_mat, 2000)
    print(a_res.mean(axis=0))

test_correlated_norm()