from time import sleep
infos = list()
langu = list()
account = str(input("Put the Name of you GitHub account: ")).strip()
insta = str(input("Put The Name Of your Instagram Account (N/A to don't put): ")).strip()
social = ""
insta = f'https://www.instagram.com/{insta}/'
if insta != "https://www.instagram.com/N/A/":
    social = f'<a href="{insta}" target="_blank"><img src="https://img.shields.io/badge/'\
             '-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=black"></a>'
else:
    social = "### None"
print("Put 3 Information of YOU!")
sleep(3)
for i in range(1, 4):
    infos.append(str(input(f"Put The {i}st Information: ")))
lannum = int(input("how Many programming languages you know? "))
for l in range(1, lannum + 1):
    langu.append(str(input(f"Put The Name Of the {l}st language: ")))
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
     <li><a href="https://www.python.org" target="_blank" rel="external">Python🐍</a>     
     <li><a href="https://www.mysql.com" target="_blank" rel="external">MySQL💸🎲</a> 
     <li><a href="https://code.visualstudio.com" target="_blank" rel="external">HTML5💻</a>  
     <li><a href="https://code.visualstudio.com" target="_blank" rel="external">CSS3💻</a>   
     <li><a href="https://nodejs.org/en/" target="_blank" rel="external">JavaScript💻</a>    

 </ul>
 <br>
 <hr>
 <div>
  <a href="https://github.com/{account}">
  <img height="120em" src="https://github-readme-stats.vercel.app/api?username={account}&layout=compact&hide_title=true&hide_border=true&show_icons=true&include_all_commits=true&line_height=21&bg_color=0,420000,120042&theme=dark">
  <img height="120em" src="https://github-readme-stats.vercel.app/api/top-langs/?username={account}&layout=compact&include_all_commits=true&show_icons=true&line_height=21&bg_color=0,420000,120042&theme=dark"></a>
</div>
 
 
 
<hr>
 <h1>Social Medias</h1>
<div> 

  {social}
 
 <h1>Visits!</h1>
 </div> 

![Visitor Count](https://profile-counter.glitch.me/{account}/count.svg)
"""

print(text)
