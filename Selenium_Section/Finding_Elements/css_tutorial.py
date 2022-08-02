#https://www.w3schools.com/cssref/css_selectors.asp

# css selector best selecter after ID
# fast for selenium next to ID
# easy to write
# better than xpath

#=========
# Use id or class as css selector
# '.' is for class
# '#' is for id

# http://demostore.supersqa.com/

# example: find the nav bar
# css using id = "#site-navigation"
# css using id = "nav#site-navigation"
# css using class = .main-naviagtion
# css using class = nav.main-navigation

# Two ways to test selector on Chrome developer tools/inspect
# 1. search (ctrl + f) then nav#site-navigation
# 2. use the console
#       $$(nav#site-navigation) use $$ on console for css
# Example '.product' to find all products

#=============

########CHILD ELEMENT###########
# can chain css with '>' or ' ' (space)to find child elements
# '>' for direct descendant
# ' ' for any child/subchild
# next two should give same result
# 'div.storefront-sorting ul.page-numbers'
# 'div.storefront > nav.woocommerce-pagination > ul.page-numbers

######  MORE CHILD ELEMENT ########
# locator:nth-child(n)
# locator:nth-of-type(n)
# 'ul.products li:nth-child(2)'
# 'ul.products li:nth-of-type(2)'
# EXAMPLE
# 'input.input-text:nth-of_type(1)' >> results with 4 elements
# 'input.input-text:nth_child(1)' >> results with 2 elements

######  MULTIPLE CLASSES  #########
# Conenct all classes with '.'
# 'li.product.type-product.instock.product-type-simple'
# 'li.product.type-product.outofstock'
# li,product.product-type-variable


###### USE ANY ATTRIBUTE  ######
# * 'a[data-product_id="23"]'
# * ('nav[aria-label="Primary Navigation"]')
# * ('a[aria-label="Add “Album” to your cart"]')
# * 'ul[id="site-header-cart"] a[title="View your shopping cart"]'
# * 'a[title="View your shopping cart"]'
# * 'a.footer-cart-contents[title="View your shopping cart"]'
# 'button.woocommerce-button[value="Log in"]'


###### PARTIALLY MATCHING ATTRIBUTES #######
# * contains word
# ^ starts with word
# $ ends with word
# the following 4 css have the same result
#
# 'a[title="View your shopping cart"]'
# 'a[title^="view your"]'
# 'a[title*="shopping"]'
# 'a[title$="cart"]'