import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')

# all = "Learn full-stack web development with interactive courses | codedamnOpen main menucodedamnLearning PathsContact UsPricingSearch for a courseSign InCreate accountSign inLearning PathsContact UsPricingAll coursesFull Stack Learning PathPlaygroundscodedamnOpen main menuStart learningPlaygroundsPricingContact UsSign inCreate AccountFull-stack learning pathBecome a full-stack web developer by learning through interactive coursesWeb 3.0 And BlockchainBetaStart your Web 3.0 journey building with ethereum, solidity, and more.Python MasteryBetaBecome a full-stack web developer by learning through interactive coursesExplore All PathsStart a practice playgroundPractice anything inside browser without any download/setupSolidityHTML/CSSReactVue 3Next.jsNode.jsPythonBuild a projectBuild projects, get community feedback and gain confidence.Explore frontend projectsExplore backend projectsExplore full stack projectsTake part in#100DaysOfProjectsAttempt this week's challengeLearn ProgrammingInteractivelyBuild projects, practice and learn to code from scratch - without leaving your browser.Explore All RoadmapsGet out of tutorial hellVideos are so 2008-ish...You have read about "Practice makes a man perfect", but you still learn by watching hours of videos.For the first time ever, you can experience an interactive course completely online - a perfect blend of theory and practice right inside your browser.10x more engaging, higher quality, cheaper, and a stellar experience for visual learners.Learn moreLaurentiu PopafromRomaniaFrontend web developer atAgile MediaI was from non-tech background and was confused about what to learn and what steps to take. I managed to make a professional conversion at the age of 40, and even get my first job in the IT field. Possibility to have structured courses and codelabs in one place oncodedamn is game changer.Darshil RathodfromIndiaFull-stack developer atBlueLearnWith codedamn I was able to fill up loopholes in my knowledge, learn new cutting edge technologies in full-stack development like Next JS.Everything I needed was there in one placewith hands-on practice labs.Adeseye KayfromNigeriaFrontend Developer atIngenious CodesI've tried several coding bootcamps but the quality and structural approach to be a fullstack developer has never been clearer until I joined codedamn.Doing the practice on labs, I am now confident in my coding ability.Joining codedamn has been one of my best life decisions.Aswin CGfromIndiaCSE undergrad and mentor atFOSS OpenHackCodedamn is the platform wheretheory meets practice. The course contents are precise and to the point and the projects are well designed to give hands-on practice. Highly recommended if someone wants to get the real coding experience for web development jobs or internships.Structured RoadmapsWhat should I learnafter?Chances are that you're NOT willing to spend years of your time figuring out the right tech stack. We got you. Our industry experts figured out a perfect learning path for you that is short, complete, and fully relevant in2022. Seriously.Learn more1h interactive courseInternet Fundamentals5h interactive courseHTML/CSS Fundamentals2h interactive courseAdvanced HTML5/CSS34h interactive courseJavaScript Essentials10h interactive coursePractice JavaScript with 10+ Projects4h interactive courseAdvanced Practical JavaScript1h interactive courseUsing DevTools2h interactive courseVersion Control System2h interactive courseNPM and Yarn5h interactive courseReact Fundamentals1h interactive courseTailwind CSS Fundamentals2h interactive courseReact Query for network requests2h interactive courseAdvanced React Hooks1h interactive courseAdvanced React Concepts3h interactive course5 React Projects2h interactive courseAdvanced Theoretical JavaScript2h interactive courseTesting Code with Cypress1h interactive courseFrontend Certification Exam2h interactive courseLinux Fundamentals1h interactive courseNode.js Fundamentals2h interactive courseAdvanced Node.js Concepts2h interactive courseWorking with MongoDB4h interactive courseUnderstanding GraphQL2h interactive courseBuilding production apps with Next.js1h interactive courseAdvanced Next.js Concepts2h interactive courseCaching with Redis2h interactive courseTypeScript Fundamentals1h interactive courseCI/CD with GitHub Actions1h interactive courseWriting secure web apps1h interactive courseFull Stack Certification Exam1h interactive courseFull Stack Real Interview QuestionsWe got your backNever learn alone.The best part about learning with friends is learning with friends. We tightly integrate our learning platform with our Discord community of learners, teachers, and our reward system.Ask questions 24x7, answer questions of others, gain XP, complete the courses and grow together.Join our discord serverOver 60,000+ people use codedamn today.Learn modern programming skills and become eligible to work at top companies.Explore All Learning PathsFooterLearn to code interactively - without ever leaving your browser.FacebookInstagramTwitterGitHubYouTubeSolutionsLearning pathsBecome a full stack web developerWhat programming language should I learn?SupportContact usPricingCreate a free accountCompanyBlogCareersWrite on codedamnCampus AmbassadorRefer & earnLegalPrivacyTerms© codedamn™2022| All rights reserved."


# res = requests.get('https://codedamn.com')
res = requests.get('https://stackoverflow.com/')

soup = BeautifulSoup(res.content, 'html.parser')

# tit = soup.title.text
# paragraphs = soup.select('p')


# Removing html tags from response soup
good = ''.join(soup.stripped_strings)

print(good)
print(type(good))

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
no_punc = ""
for char in good:
    if char not in punctuations:
        no_punc = no_punc + char

print(no_punc)
print(type(no_punc))

splitted = no_punc.split()
print(splitted)
print(type(splitted))

unique_words = []
for i in splitted:
    if not i in unique_words:
        unique_words.append(i)
print(unique_words)

txt = res.text
status = res.status_code
# print(txt, status)
print(status)
# print(tit)
# print(paragraphs)












def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
