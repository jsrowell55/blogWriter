def medium(driver, url):
    # get title and subtitle from medium blog post -----------------------------
    driver.get(url)

    title = driver.find_element("tag name", "h1").text
    subtitle = driver.find_element("tag name", "h2").text
    title = title + " - " + subtitle
    
    return title