import pytest
import subprocess
'''
把他当固定模板,知道改那个位置就可以
'''
if __name__ == '__main__':
    # pytest运行测试用例的命令
    #pytest.main(['-sv', './case/test_order.py','--alluredir=./reports/mtx','--clean-alluredir'])
    pytest.main(['-sv', './case/test_cart.py','--alluredir=./reports/mtx','--clean-alluredir'])
    # subprocess: 把在终端操作的命令行转移到python文件中操作,shell=True 接收这个命令，并以shell脚本的形式运行
    subprocess.call('allure generate ./reports/mtx -o ./reports/html/ --clean',shell=True)