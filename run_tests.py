from tests import test_driver

'''
there is a great answer to why you can't run tests directly from the command line
here: https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912
this file is necessay to run tests because of the way Python relative imports work
'''

driver = test_driver.TestFantasyAnalysisDriver()
driver.test_create_player_db()
