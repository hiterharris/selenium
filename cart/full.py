def full(WebDriverWait, driver, EC, By, TimeoutException, address, product):
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


    # selectProduct
    try:
        print("Product-Selection page ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Select Plan")]'))).click()
    except TimeoutException:
        print("Product-Selection page timeout")

    # contact
    try:
        print("Contact page ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "first-name"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(User.first)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(User.last)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "email-address"))).send_keys(User.email)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "phone-number"))).send_keys(User.phone)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Next")]'))).click()
    except TimeoutException:
        print("Contact-Credit page timeout")

    # driver.find_element('xpath', '// span[contains(text(), "Next")]').click()



    # credit
    try:
        print("Credit page ready")
        
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "react-select-3-input"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "react-select-3-input"))).send_keys(User.month)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "react-select-4-input"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "react-select-4-input"))).send_keys(User.month)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "react-select-5-input"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "react-select-5-input"))).send_keys(User.month)


        # WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Month")]'))).click()
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@aria-label="birth-month"]'))).send_keys(User.month)
        # keyboard.send("enter")

        # WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Day")]'))).click()
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@aria-label="birth-day"]'))).send_keys(User.day)
        # keyboard.send("enter")

        # WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Year")]'))).click()
        # WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@aria-label="birth-year"]'))).send_keys(User.year)
        keyboard.send("enter")

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "ssn"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "ssn"))).send_keys(User.ssn)

        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Submit")]'))).click()
    except TimeoutException:
        print("Credit page timeout")


    # installation
    try:
        print("Installation ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[@aria-disabled="false"]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Next")]'))).click()
    except TimeoutException:
        print("Installation timeout")

    # payment
    try:
        print("Payment ready")
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "autopay"))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// label/div[@class="checkbox"]'))).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Submit Order")]'))).click()
    except TimeoutException:
        print("Payment timeout")

    # confirmation
    try:
        print("Confirmation ready")
        confirmation = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// *[contains(text(), "Confirmation")]')))
        print('confirmation: ', confirmation)
    except TimeoutException:
        print("Confirmation timeout")