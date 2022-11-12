from pages.base_page import BasePage


class Dashboard(BasePage):
  scouts_panel_xpath = "//*/header/div/h6"
  main_page_menu_xpath = "//*[text()='Main page']"
  players_menu_xpath = "//*ul[1]/div[2]/div[2]/span"
  language_menu_xpath = "//*/ul[2]/div[1]/div[2]/span"
  sign_out_menu_xpath = "//*/ul[2]/div[2]/div[2]/span"
  players_count_block_xpath = "//*main/div[2]/div[1]/div"
  matches_count_block_xpath = "//*/main/div[2]/div[2]/div"
  reports_count_block_path = "//*/main/div[2]/div[3]/div"
  events_count_block_xpath = "//*/main/div[2]/div[4]/div"
  add_player_button_xpath = "//*[text()='Add player']"

  pass
