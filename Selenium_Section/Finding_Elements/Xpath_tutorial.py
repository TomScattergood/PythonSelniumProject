"""
//relative  xpath
/ absolute path

//tag[@attribute='value']
//*[@attribute='value']

$x in developer console
"""


#('//ul[@id="site-header-cart"]')   relative xpath
# ('/html/body/div[2]/header/div[2]/div/ul')    absolute xpath

# ('//ul[contains(@id, "site-header-cart")]')
# ('//ul[contains(@id, "site")]')    partial search also works

# ('//a[text()="Lost your password?"]')
# ('//a[contains(text(), "Lost your password?")]')
# ('//a[contains(text(), "password?")]')