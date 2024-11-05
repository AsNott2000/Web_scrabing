from bs4 import BeautifulSoup
import pandas as pd

box1_html = """<div class="Box klGMtt"><div display="flex" class="Box Flex fJFHNR bnpRyo"><span class="Text iQPLNb">Maç</span></div><div class="Box klGMtt"><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Toplam Maç</span><span color="onSurface.nLv1" class="Text ietnEf">10 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">İlk 11</span><span color="onSurface.nLv1" class="Text ietnEf">4 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Maç Başına Dakika</span><span color="onSurface.nLv1" class="Text ietnEf">40</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Toplam oynanan dakika</span><span color="onSurface.nLv1" class="Text ietnEf">404 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Haftanın Takımı</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div></div></div>"""

soup_box1html = BeautifulSoup(box1_html,"html.parser")
soup_box1html.prettify()

box_1 = soup_box1html.find_all("div", attrs={"class": "Box Flex dlyXLO bnpRyo"})

matches_box = box_1[0]
lineup_box = box_1[1]
permin_box = box_1[2]
summin_box = box_1[3]
weekteam_box = box_1[4]

matches = matches_box.find_all("span", attrs={"class": "Text ietnEf"})

print(matches[0].get_text(separator=" ", strip=True))
print(matches[1].text)

lineups = lineup_box.find_all("span", attrs={"class": "Text ietnEf"})

print(lineups[0].get_text(separator=" ", strip=True))
print(lineups[1].text)

permin = permin_box.find_all("span", attrs={"class": "Text ietnEf"})

print(permin[0].get_text(separator=" ", strip=True))
print(permin[1].text)

summin = summin_box.find_all("span", attrs={"class": "Text ietnEf"})

print(summin[0].get_text(separator=" ", strip=True))
print(summin[1].text)

weekteam = weekteam_box.find_all("span", attrs={"class": "Text ietnEf"})

print(weekteam[0].get_text(separator=" ", strip=True))
print(weekteam[1].text)


print("________________________________________________")

box2_html = """<div class="Box klGMtt"><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Gol</span><span color="onSurface.nLv1" class="Text ietnEf">2 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Gol Beklentisi (xG)</span><span color="onSurface.nLv1" class="Text ietnEf">3.90 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Gol Sıklığı</span><span color="onSurface.nLv1" class="Text ietnEf">202 min</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Maç Başına Gol</span><span color="onSurface.nLv1" class="Text ietnEf">0.2</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Maç Başına Şut</span><span color="onSurface.nLv1" class="Text ietnEf">2.4</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Maç Başına İsabetli Şut</span><span color="onSurface.nLv1" class="Text ietnEf">1.1</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Kaçan Büyük Şans</span><span color="onSurface.nLv1" class="Text ietnEf">8 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Pozisyonu Gole Çevirme</span><span color="onSurface.nLv1" class="Text ietnEf">8%</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Penaltı Golü</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Penaltıyı gole çevirme yüzdesi</span><span color="onSurface.nLv1" class="Text ietnEf">0%</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Serbest Vuruş Golü</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Duran Topu Gole Çevirme</span><span color="onSurface.nLv1" class="Text ietnEf">0%</span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Ceza Sahası İçinden Gol</span><span color="onSurface.nLv1" class="Text ietnEf">2/24 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Ceza Sahası Dışından Gol</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Kafa Golü</span><span color="onSurface.nLv1" class="Text ietnEf">2 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Sol Ayak Golü</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Sağ Ayak Golü</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div><div display="flex" class="Box Flex dlyXLO bnpRyo"><span color="onSurface.nLv1" class="Text ietnEf">Kazanılan Penaltı</span><span color="onSurface.nLv1" class="Text ietnEf">0 </span></div></div>"""

soup_box2html = BeautifulSoup(box2_html,"html.parser")
soup_box2html.prettify()

box_2 = soup_box2html.find_all("div", attrs={"class": "Box Flex dlyXLO bnpRyo"})

goal_box = box_2[0]
xg_box = box_2[1]
permingoal_box = box_2[2]
permatchgoal_box = box_2[3]
permathcshoot_box = box_2[4]
permathcshootontarget_box = box_2[5]
missesbigchance_box = box_2[6]
pozitiongoalratio_box = box_2[7]
penaltygoal_box = box_2[8]
penaltygoalratio_box = box_2[9]
freekickgoal_box = box_2[10]
freekickgoalratio_box = box_2[11]
goalinbox_box = box_2[12]
goaloutbox_box = box_2[13]
headgoal_box = box_2[14]
leftfootgoal_box = box_2[15]
rightfootgoal_box = box_2[16]
wonpenalty_box = box_2[17]

goals = goal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(goals[0].get_text(separator=" ", strip=True))
print(goals[1].text)

xg = xg_box.find_all("span", attrs={"class": "Text ietnEf"})

print(xg[0].get_text(separator=" ", strip=True))
print(xg[1].text)

permingoal = permingoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(permingoal[0].get_text(separator=" ", strip=True))
print(permingoal[1].text)

permatchgoal = permatchgoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(permatchgoal[0].get_text(separator=" ", strip=True))
print(permatchgoal[1].text)

permathcshoot = permathcshoot_box.find_all("span", attrs={"class": "Text ietnEf"})

print(permathcshoot[0].get_text(separator=" ", strip=True))
print(permathcshoot[1].text)

permathcshootontarget = permathcshootontarget_box.find_all("span", attrs={"class": "Text ietnEf"})

print(permathcshootontarget[0].get_text(separator=" ", strip=True))
print(permathcshootontarget[1].text)

missesbigchance = missesbigchance_box.find_all("span", attrs={"class": "Text ietnEf"})

print(missesbigchance[0].get_text(separator=" ", strip=True))
print(missesbigchance[1].text)

pozitiongoalratio = pozitiongoalratio_box.find_all("span", attrs={"class": "Text ietnEf"})

print(pozitiongoalratio[0].get_text(separator=" ", strip=True))
print(pozitiongoalratio[1].text)

penaltygoal = penaltygoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(penaltygoal[0].get_text(separator=" ", strip=True))
print(penaltygoal[1].text)

penaltygoalratio = penaltygoalratio_box.find_all("span", attrs={"class": "Text ietnEf"})

print(penaltygoalratio[0].get_text(separator=" ", strip=True))
print(penaltygoalratio[1].text)

freekickgoal = freekickgoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(freekickgoal[0].get_text(separator=" ", strip=True))
print(freekickgoal[1].text)

freekickgoalratio = freekickgoalratio_box.find_all("span", attrs={"class": "Text ietnEf"})

print(freekickgoalratio[0].get_text(separator=" ", strip=True))
print(freekickgoalratio[1].text)

goalinbox = goalinbox_box.find_all("span", attrs={"class": "Text ietnEf"})

print(goalinbox[0].get_text(separator=" ", strip=True))
print(goalinbox[1].text)

goaloutbox = goaloutbox_box.find_all("span", attrs={"class": "Text ietnEf"})

print(goaloutbox[0].get_text(separator=" ", strip=True))
print(goaloutbox[1].text)

headgoal = headgoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(headgoal[0].get_text(separator=" ", strip=True))
print(headgoal[1].text)

leftfootgoal = leftfootgoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(leftfootgoal[0].get_text(separator=" ", strip=True))
print(leftfootgoal[1].text)

rightfootgoal = rightfootgoal_box.find_all("span", attrs={"class": "Text ietnEf"})

print(rightfootgoal[0].get_text(separator=" ", strip=True))
print(rightfootgoal[1].text)

wonpenalty = wonpenalty_box.find_all("span", attrs={"class": "Text ietnEf"})

print(wonpenalty[0].get_text(separator=" ", strip=True))
print(wonpenalty[1].text)

print("________________________________________________")

data = [[matches[1].text,
            lineups[1].text,
            permin[1].text,
            summin[1].text,
            weekteam[1].text,
            goals[1].text,
            xg[1].text,
            permingoal[1].text,
            permatchgoal[1].text,
            permathcshoot[1].text,
            permathcshootontarget[1].text,
            missesbigchance[1].text,
            pozitiongoalratio[1].text,
            penaltygoal[1].text,
            penaltygoalratio[1].text,
            freekickgoal[1].text,
            freekickgoalratio[1].text,
            goalinbox[1].text,
            goaloutbox[1].text,
            headgoal[1].text,
            leftfootgoal[1].text,
            rightfootgoal[1].text,
            wonpenalty[1].text
    ]]
df = pd.DataFrame(data, columns=["Matches","Lineups","permin","summin","weekteam","goals","xg","permingoal","permatchgoal","permathcshoot","permathcshootontarget","missesbigchance","pozitiongoalratio","penaltygoal","penaltygoalratio","freekickgoal","freekickgoalratio","goalinbox","goaloutbox","headgoal","leftfootgoal","rightfootgoal","wonpenalty"])
df.to_csv('ennesyri.csv', index=False)


