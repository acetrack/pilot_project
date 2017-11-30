import time
import unittest
from django.urls import reverse

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:8080'
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def _test_show_the_welcome_message(self):
        # 사용자는 사전 앱을 알게 되어 홈페이지에 방문한다
        self.browser.get(self.base_url)

        time.sleep(1)

        # 홈페이지에 방문하고 보니 제목이 "Acetrack's work space!!!"인 것을 보고 홈페이지에 올바르게 방문한 것을 확인한다
        self.assertEqual('Acetrack\'s work space!!!', self.browser.title)

        # 환영의 글이 보이고
        div_area = self.browser.find_element_by_id('id_welcome_message')
        self.assertTrue(div_area, "Add a Welcome message!")

        # 네비게이션이 보이고 (홈 / 블로그 / 사전)
        div_area = self.browser.find_element_by_id('id_navigation')
        self.assertTrue(div_area, "Add a navigation bar!")

        # 로그인을 할 수 있도록 입력하는 부분이 있고
        form_area = self.browser.find_element_by_id('id_login_form')
        self.assertTrue(form_area, "Add a login form")

        # 회원가입 버튼이 있다.
        btn_sign_up = self.browser.find_element_by_id('id_sign_up_btn')
        self.assertTrue(btn_sign_up, "Add a button for sign-up")

        self.fail("테스트 종료")

    def _test_show_sign_up(self):
        # 사용자는 사전 앱을 알게 되어 홈페이지에 방문한다
        self.browser.get('http://localhost:8080/account/sign_up')

        time.sleep(3)

        # 에 '회원가입'이라고 되어있다
        self.assertEqual('회원가입', self.browser.title)
        time.sleep(3)

        self.fail("테스트 종료")

    def test_show_login(self):
        self.browser.get(self.base_url + reverse('account:login'))
        self.assertEqual(reverse('account:login'), '/account/login/')
        # 화면에 'login'이라고 되어있다
        self.assertEqual('Login', self.browser.title)

        # id_username에 'acetrack'을 입력한다
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('acetrack')

        # id_password에 'sy2735928'을 입력한다
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('sy2735928')

        # submit 버튼을 누른다
        self.browser.find_element_by_tag_name("button").click()


        time.sleep(10)

        self.fail("테스트 종료")

        # time.sleep(3)

        # self.fail("테스트 종료")


    # def test_show_the_blog(self):
    #     # 사용자는 블로그 첫 화면을 본다
    #     self.browser.get('http://localhost:8080/blog')
    #     # 환영의 글이 보여진다
    #     header_text = self.browser.find_element_by_tag_name('h1').text
    #     self.assertEqual('진화하는 개인사전', header_text)
    #
    #     # 로그인을 할 수 있는 화면이 보여진다
    #     inputbox = self.browser.find_element_by_name('id_username')
    #     self.assertEqual(inputbox.get_attribute('placeholder'), 'ex) acetrack')
    #     inputbox.send_keys('acetrack')
    #
    #     time.sleep(1)
    #
    #     # ID 입력 / PW 입력한다
    #     inputbox = self.browser.find_element_by_name('id_password')
    #     self.assertEqual(inputbox.get_attribute('placeholder'), 'ex) ********')
    #     inputbox.send_keys('passssss')
    #
    #     # 회원가입으로 연결하는 link가 보여진다
    #     link_text = self.browser.find_element_by_tag_name('a').text
    #     self.assertEqual('회원가입', link_text)
    #
    #
    #     # 일정을 입력할 수 있는 페이지로 바로 이동한다
    #     # inputbox = self.browser.find_element_by_id('id_new_item')
    #     # self.assertEqual(inputbox.get_attribute('placeholder'), '할일을 입력하세요')
    #
    #     # 사용자는 생일날 미역국을 끓이기 위해 텍스트박스에 '시장에서 미역 사기'를 입력한다
    #     # inputbox.send_keys('시장에서 미역 사기')
    #
    #     # 사용자가 엔터를 입력하면 페이지를 새로고침해서 모든 일정 목록을 보여준다
    #     # "1: 시장에서 미역 사기"가 첫 번째 할 일로 일정 목록에서 보여진다
    #     # inputbox.send_keys(Keys.ENTER)
    #     # time.sleep(1)
    #
    #     # table = self.browser.find_element_by_id('id_list_table')
    #     # rows = table.find_elements_by_tag_name('tr')
    #     # self.assertTrue(
    #     #     any(row.text == '1: 시장에서 미역 사기' for row in rows),
    #     #     "New to-do item did not appear in table"
    #     # )
    #
    #     # 사용자는 추가로 할 일 텍스트박스에 입력할 수 있고
    #     # "미역을 물에 불리기"라고 입력한다
    #
    #     time.sleep(3)
    #
    #     self.fail('테스트 종료')
    #
    #     # 다시 페이지를 새로고침해서 입력한 일정 두 가지 모두 목록에 표시한다
    #
    #     # 사용자는 일정 목록이 사이트에 올바로 저장되었는지 궁금해서
    #     # 고유 URL 생성을 확인한다
    #
    #     # 사용자는 URL을 방문하고 일정 목록이 올바르게 있음을 확인한다
    #
    #     # 사용자는 이제 만족하고 잠을 자러간다



if __name__ == '__main__':
    unittest.main(warnings='ignore')