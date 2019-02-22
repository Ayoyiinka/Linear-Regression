from selenium import webdriver
import os

os.chdir('C:\\Users\\Ayoyinka Obisesan\\Desktop')
with open('footballData.csv', 'w') as f:
    f.write('Player name,Position,Age,Market Value,NaN,Matches,\
            Goals,Own Goals,Assists,Yellow cards,Second Yellow card,\
	    Red Cards,Substitued on,Substituted off\n')

browser = webdriver.Firefox()
finalList = []
for i in range(1,21):
    url = 'https://www.transfermarkt.co.in/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&alters\
    klasse=alle&ausrichtung=alle&jahrgang=0&land_id=0&page=' + str(i) + '&plus=1&spielerposition_id=alle'
    browser.get(url)
    detailsOdd = browser.find_elements_by_class_name('odd')
    detailsEven = browser.find_elements_by_class_name('even')
    for i in range(len(detailsOdd)):
        textDetailsOdd = detailsOdd[i].text
        listDetailsOdd = textDetailsOdd.split('\n')
        endListStringOdd = listDetailsOdd[-1]
        endListListOdd = endListStringOdd.split(' ')
        minusEndListOdd = listDetailsOdd[1:-1]
        for k in range(len(endListListOdd)):
            minusEndListOdd.append(endListListOdd[k])
            
        print(minusEndListOdd)
        finalList.append(minusEndListOdd)    
    
    for i in range(len(detailsEven)):
        textDetailsEven = detailsEven[i].text
        listDetailsEven = textDetailsEven.split('\n')
        endListStringEven = listDetailsEven[-1]
        endListListEven = endListStringEven.split(' ')
        minusEndListEven = listDetailsEven[1:-1]
        for k in range(len(endListListEven)):
            minusEndListEven.append(endListListEven[k])
            
        print(minusEndListEven)
        finalList.append(minusEndListEven)

browser.close()

with open('footballData.csv', 'a') as f:
    for i in range(len(finalList)):
        newList = finalList[i]
        f.write(newList[0]+','+newList[1]+','+newList[2]+','+newList[3]+','+newList[7]+','+newList[8]+','+newList[9]+','+newList[10]+\
                ','+newList[11]+','+newList[12]+','+newList[13]+','+newList[14]+','+newList[15]+','+'\n')









