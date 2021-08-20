from time import sleep

try:
    arq = open("../README.md", "rt")
    arq.close()
except FileNotFoundError:
    arq = open("../README.md", "wt+")
    print("O Arquivo Foi Criado")
else:
    print("O Arquivo Já Existe")

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
print("---" * 15)
account = str(input("Coloque O nome da sua conta GitHub: ")).strip()
print("---" * 15)
insta = str(input("Coloque O nome da sua conta Instagram (N/A Para Não Colocar): ")).strip()
print("---" * 15)
theme = str(input("Coloque O nome Do tema (https://github.com/AthosFB/README.md-Creator/"
                  "tree/main/files/Themes/All%20Themes): ")).strip().lower()
print("---" * 15)
social = ""
insta = f'https://www.instagram.com/{insta}/'
if insta.lower() != "https://www.instagram.com/n/a/":
    social = f'<a href="{insta}" target="_blank"><img src="https://img.shields.io/badge/'\
             '-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=black"></a>'
else:
    social = "### None"

print("Coloque 3 informações sobre VOCÊ!")
sleep(2)
for i in range(1, 4):
    infos.append(str(input(f"Coloque a {i}º Informação: ")))

lannum = int(input("Quantas Linguagens de Programação você conhece? "))
for l in range(1, lannum + 1):
    langu.append(str(input(f"Coloque o Nome Da {l}º linguagem: ")).lower().strip())
for lan in langu:
    langutxt.append(f'<li>{lan.title()}<br>')
for i in langutxt:
    lantxtfinal = f"""{lantxtfinal} 
{i}
"""

for k, i in proling.items():
    if k in langu:
        know = f"""{know}
{i}
"""
if len(know) == 0:
    know = "Outros"
text = f"""
# Bem Vindo Ao Meu Perfil!
***
### Dá uma Olhada nos Meus Projetos!

<hr>

 - {infos[0]}
 - {infos[1]}
 - {infos[2]}

 <hr>
 <ul type="square">
     <p>
        {lantxtfinal} 

 </ul>
 <hr>
 <div>
  <a href="https://github.com/{account}">
  <img height="120em" src="https://github-readme-stats.vercel.app/api?username={account}&layout=compact&hide_title=true&hide_border=true&show_icons=true&include_all_commits=true&line_height=21&theme={theme}">
  
  <img height="120em" src="https://github-readme-stats.vercel.app/api/top-langs/?username={account}&layout=compact&include_all_commits=true&show_icons=true&line_height=21&theme={theme}"></a>
</div>

***

### Conhecimentos

<div style="display: inline_block"><br>
{know}
</div>
 
***
 
<hr>
 <h1>Mídias Sociais</h1>
<div> 

  {social}
 
 ***
 
 <h1>Visitas!</h1>
 </div> 

![Visitor Count](https://profile-counter.glitch.me/{account}/count.svg)
"""

try:
    arq.write(text)
except:
    print("Ocorreu Um Erro")
else:
    print("Seu Arquivo Foi Criado!")
