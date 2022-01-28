import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import json
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

Name = "Parthiv Chandran"
Title = 'Software Developer'
Contact = "Kendriya Vihar Apartments, Yelahanka, \n Bangalore \n 560064 \n Karnataka, India. \n 9538883326  \n parthiv.c2002@gmail.com"
ProjectsHeader = 'PROJECTS/PUBLICATIONS'
ProjectOneTitle = 'Online CV Builder'
ProjectOneDesc = "Built an online cv builder using python\nIntegrated with encryption and fernet"
ProjectTwoTitle = 'Fitness Tracker'
ProjectTwoDesc = "Built a fitness tracker that tracks calories \n Calories burnt based on steps"
ProjectThreeTitle = 'Tenjiku Haven'
ProjectThreeDesc = "Built an automated invoice maker for a clothing brand"
Linkedin = "ParthivChandran"
WorkHeader = 'EXPERIENCE'
WorkOneTitle = "Tenjiku Haven"
WorkOneTime = "1 year"
WorkOneDesc = "Was a website designer for Tenjiku Haven"
WorkTwoTitle = "Game Developer"
WorkTwoTime = "2 years"
WorkTwoDesc = "Developed games for Unity"
WorkThreeTitle = "Backend Developer At Google"
WorkThreeTime = "6 years"
WorkThreeDesc = "Did the backened part of HPs website"
EduHeader = 'EDUCATION'
EduOneTitle = "Amrita School Of Engineering"
CGPA = '9.0'
EduOneDesc = 'Computer Science Engineering'
SkillsHeader = 'Skills'
SkillsDesc = "- Python\n- C\n- C++\n- CSS\n- Javascript\n- Game Development on Unity\n- BooScript\n- SQL\n- Data Structures\n- Data Manipulation\n- Data Science"
ExtrasTitle = 'ACTIVITIES'
ExtrasDesc = "State Level Basketball Player \nState Level Taekwondo Athlete\nCompetetive Programmer\n5 Star Rating on Codechef "


plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)


ax.set_facecolor('white')


plt.axis('off')


plt.annotate(Name, (.25, .94), weight='bold', fontsize=20)
plt.annotate(Title, (.30, .91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7, .906), weight='regular',
             fontsize=8, color='#ffffff')
plt.annotate(ProjectsHeader, (.02, .86), weight='bold',
             fontsize=10, color='#58C1B2')
plt.annotate(ProjectOneTitle, (.02, .832), weight='bold', fontsize=10)
plt.annotate(ProjectOneDesc, (.04, .78), weight='regular', fontsize=9)
plt.annotate(ProjectTwoTitle, (.02, .745), weight='bold', fontsize=10)
plt.annotate(ProjectTwoDesc, (.04, .71), weight='regular', fontsize=9)
plt.annotate(ProjectThreeTitle, (.02, .672), weight='bold', fontsize=10)
plt.annotate(ProjectThreeDesc, (.04, .638), weight='regular', fontsize=9)
plt.annotate(Linkedin, (.06, .6), weight='bold', fontsize=10)
plt.annotate(WorkHeader, (.02, .54), weight='bold',
             fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02, .508), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02, .493), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04, .445), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02, .4), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02, .385), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04, .337), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02, .295), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02, .28), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04, .247), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02, .185), weight='bold',
             fontsize=10, color='#58C1B2')
plt.annotate(EduOneTitle, (.02, .155), weight='bold', fontsize=10)
plt.annotate(EduOneDesc, (.02, .14), weight='regular', fontsize=9)
plt.annotate(CGPA, (.02, .125), weight='regular', fontsize=9, alpha=.6)
plt.annotate(SkillsHeader, (.7, .8), weight='bold',
             fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7, .56), weight='regular',
             fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.7, .43), weight='bold',
             fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.7, .345), weight='regular',
             fontsize=10, color='#ffffff')

arr_code = mpimg.imread('images/face.png')
imagebox = OffsetImage(arr_code, zoom=0.3)
ab = AnnotationBbox(imagebox, (.1, .94))
ax.add_artist(ab)

img = mpimg.imread('images/linkedin.png')
imagebox1 = OffsetImage(img, zoom=0.3)
ab1 = AnnotationBbox(imagebox1, (.03, .605))
ax.add_artist(ab1)

plt.savefig('builder/resumeexample.png', dpi=300, bbox_inches='tight')
plt.savefig('builder/resumeexample.pdf', dpi=300, bbox_inches='tight')


with open('database/user.json', 'rb') as file:
    original = file.read()
