
def products(WebDriverWait, driver, EC, By, TimeoutException, address, product):
    # serviceability
    try:
        print("Address Check page ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "street-address"))).send_keys(address)
        WebDriverWait(driver, 130).until(EC.presence_of_element_located((By.ID, 'react-select-2-option-0'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Check availability")]'))).click()
    except TimeoutException:
        print("Address Check pageage timeout")


    # are you moving
    if product == 'fiber':
        try:
            print("Are you moving page ready")
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// button[@data-testid="btn-moving-yes"]'))).click()
        except TimeoutException:
            print("Are You Moving page timeout")
    else:
        pass
