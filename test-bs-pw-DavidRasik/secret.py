from playwright.sync_api import sync_playwright
import os



def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # !!!
        # na page.locator(selector) se dá použít funkce .text_content(), která vypíše text daného prvku
        # !!!

        page.goto("https://souhrada.github.io/playwright-exam/")
        page.fill('input#login', "Jarmil")
        page.fill('input#login', "Admin123")
        page.click('button.login-btn')

        tajnost = page.locator('p.super-secret-text').text_content()
        print(tajnost)

        # page = get.n


        browser.close()
    

if __name__ == "__main__":
    main()
