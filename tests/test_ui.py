from argparse import Action
import pytest
import re

from playwright.sync_api import Page, expect
@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):
    #Arrange
    page.goto("https://demo.applitools.com")

    #Act
    page.locator('id=username').fill('andy')
    page.locator('id=password').fill('i<3pandas')
    page.locator('id=log-in').click()

    # Assert
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()
    expect(page.get_by_text('Pay Now')).to_be_visible()
