# Task 1: software configuration

## Subtask 1: Why did I choose to participate in the Dare IT Challenge?


I decide to participate in this project because of staring my career in IT, or rather in QA, in Poland. 
So I need some structured knowledge and practice before I would start applying for my first job.

My goal is to feel more confident on my first interviews, to have some portfolio on my GitHub and,
of course, knowledge to be able to work as a Junior QA. 
I understand that it is only beginning of my studying, 
but it always the most difficult.


## Have a nice day! 🙂

##                     *Julia*




# Task 2: Selectors

## Elements:
## 1. scouts_panel_xpath

//*/div/div[1]/h5

//*[text()="Scouts Panel"]

//child::div/h5

## 2. login_field_xpath
 
//*/div/div[1]/div[1]/div

//*[@id='login']

//*[@name='login'] 

## 3. password_field_xpath

//*/div/div[1]/div[2]/div

//*[@id='password']

//*[@name='password'] 

## 4. remind_password_hyperlink_xpath

//child::div/a

//*[text()="Remind password"]

//*[@id="__next"]/form/div/div[1]/a

## 5. language_changing_xpath

//*[@id="__next"]/form/div/div[2]/div/div

//*[contains(@class, "MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input")]


## 6. sign_in_button_xpath

//*/div/div[2]/button/span[1]

//*[contains(@class, "MuiButton-label")]