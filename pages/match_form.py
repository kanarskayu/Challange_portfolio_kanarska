from pages.base_page import BasePage


class MatchForm(BasePage):
  my_team_field_xpath = "//*/div[1]/div/div/input"
  enemy_team_field_xpath = "//*/div[2]/div/div/input"
  my_team_score_field_xpath = "//*/div[1]/div/div/input"
  enemy_team_score_field_xpath = "//*/div[4]/div/div/input"
  date_field_xpath = "//*/div[5]/div/div/input"
  match_at_home_xpath = "//*[text()='Match at home']"
  match_out_home_xpath = "//*[text()='Match out home']"
  league_xpath = "//*/div[8]/div/div/input"
  submit_button_xpath = "//*[text()='Submit']"
  clear_button_xpath = "//*[text()='Clear']"

pass
