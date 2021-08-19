from time import sleep

infos = list()
langu = list()
langutxt = list()
lantxtfinal = know = ""

proling = {"python": '<img align="center" alt="Python" height="60" width="80" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">',
           "mysql": '<img align="center" alt="MySQL" height="120" width="120" src="https://waresoft.com.br/wp-content/uploads/2021/04/MySQL_Logo_600x600.png">',
           "css3": '<img align="center" alt="Athos-CSS" height="60" width="80" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg">',
           "html5": '<img align="center" alt="HTML" height="60" width="80" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">',
           "javascript": '<img align="center" alt="Js" height="60" width="80" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">',
           "js": '<img align="center" alt="Js" height="60" width="80" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">',
           "java": '<img align="center" alt="Java" height="80" width="80" src="https://alternativesoft.info/icons/java.png">',
           "php": '<img align="center" alt="Java" height="80" width="80" src="https://storage.googleapis.com/hcode.com.br/courses/1/logo_svg5f7f6e392a041.svg">',
           "c": '<img align="center" alt="Java" height="80" width="80" src="https://camo.githubusercontent.com/fa78f1cf0a8057e7dde71b15370855b874b7b39de045bf053ac344bebb71047b/68747470733a2f2f63646e2e69636f6e73636f75742e636f6d2f69636f6e2f667265652f706e672d3235362f632d70726f6772616d6d696e672d3536393536342e706e67">',
           "c++": '<img align="center" alt="Java" height="80" width="80" src="https://www.alura.com.br/artigos/assets/formacao-linguagem-c-plus-plus/img-01.png">'}

account = str(input("Put the Name of you GitHub account: ")).strip()

insta = str(input("Put The Name Of your Instagram Account (N/A to don't put): ")).strip()

theme = str(input("Put The Name Of o Theme (https://github.com/AthosFB/README.md-Creator/"
                  "tree/main/files/Themes/All%20Themes): ")).strip().lower()

social = ""
insta = f'https://www.instagram.com/{insta}/'
if insta != "https://www.instagram.com/N/A/":
    social = f'<a href="{insta}" target="_blank"><img src="https://img.shields.io/badge/'\
             '-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=black"></a>'
else:
    social = "### None"

print("Put 3 Information of YOU!")
sleep(0.000003)
for i in range(1, 4):
    infos.append(str(input(f"Put The {i}st Information: ")))

lannum = int(input("How Many Programming Languages you Know? "))
for l in range(1, lannum + 1):
    langu.append(str(input(f"Put The Name Of the {l}st language: ")))
for lan in langu:
    langutxt.append(f'<li>{lan}<br>')
for i in langutxt:
    lantxtfinal = f"""{lantxtfinal} 
{i}
"""

for k, i in proling.items():
    if k in langu:
        know = f"""{know}
{i}
"""
text = f"""
# Welcome To My Profile!
***
### See My Projects!

<hr>

 - {infos[0]}
 - {infos[1]}
 - {infos[2]}

 <hr>
 <ul type="square">
     <p>
     
        {lantxtfinal} 

 </ul>
 <br>
 <hr>
 <div>
  <a href="https://github.com/{account}">
  <img height="120em" src="https://github-readme-stats.vercel.app/api?username={account}&layout=compact&hide_title=true&hide_border=true&show_icons=true&include_all_commits=true&line_height=21&theme={theme}">
  
  <img height="120em" src="https://github-readme-stats.vercel.app/api/top-langs/?username={account}&layout=compact&include_all_commits=true&show_icons=true&line_height=21&theme={theme}"></a>
</div>

### Knowledge

{know}
 
 
<hr>
 <h1>Social Medias</h1>
<div> 

  {social}
 
 <h1>Visits!</h1>
 </div> 

![Visitor Count](https://profile-counter.glitch.me/{account}/count.svg)
"""

print(text)
