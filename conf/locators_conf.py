#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the Main page
TEMPERATURE_FIELD = "id,temperature"
BUY_BUTTON = "xpath,//button[contains(text(),'Buy %s')]"

#Product page
PAGE_HEADING = "xpath,//h2[text()='%s']"
PRODUCTS_LIST = "xpath,//div[contains(@class,'col-4')]"
ADD_PRODUCT_BUTTON = "xpath,//div[contains(@class,'col-4') and contains(.,'%s')]/descendant::button[text()='Add']"
CART_QUANTITY_TEXT = "id,cart"
CART_BUTTON = "xpath,//button[contains(@onclick,'goToCart()')]"

#Cart page
CART_TITLE = "xpath,//h2[text()='Checkout']"
CART_ROW = "xpath,//tbody/descendant::tr"
CART_ROW_COLUMN = "xpath,//tbody/descendant::tr[%d]/descendant::td"
CART_TOTAL = "id,total"

#Payment 
CARD_PAYMENT = "xpath,//span[contains(text(),'Pay with Card')]"
PAYMENT_FRAME = "//iframe[contains(@name,'stripe_checkout_app')]"
EMAIL = "xpath,//input[contains(@type,'email')]"
PHONE_NO = "xpath,//input[contains(@autocomplete,'mobile tel')]"
CARD_NUM = "xpath,////input[contains(@placeholder,'Card number')]"
CARD_DATE = "xpath//input[contains(@placeholder,'MM / YY')]"
CVV = "xpath,////input[contains(@maxlength,'4')]"
ZIP_CODE = "xpath,//input[contains(@placeholder,'ZIP Code')]" 
REMEMBER_ME_CLICK_BOX = "xpath,//div[contains(@class,'Checkbox-tick')]" 
PAY_BUTTON = "xpath,//button[contains(@type,'submit')]" 