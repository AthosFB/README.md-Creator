from time import sleep
infos = list()
langu = list()
langutxt = list()
lantxtfinal = ""

account = str(input("Put the Name of you GitHub account: ")).strip()

insta = str(input("Put The Name Of your Instagram Account (N/A to don't put): ")).strip()

theme = str(input("Put The Name Of o Theme (All The Themes are in the files): ")).strip().lower()

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
{i}"""
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
 
 
 
<hr>
 <h1>Social Medias</h1>
<div> 

  {social}
 
 <h1>Visits!</h1>
 </div> 

![Visitor Count](https://profile-counter.glitch.me/{account}/count.svg)
"""

print(text)
