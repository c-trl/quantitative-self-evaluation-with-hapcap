deck = []
asking = True
    
def asker():
    aggregator = raw_input('What item would you like to add? ')
    deck.append(aggregator)
    again = raw_input('Would you like to add another item? (y/n) ')
    if again == 'y':
            asker()
    else:
        asking == False
        df = pd.DataFrame(deck)
        name=raw_input('What is this a list of? ')
        df.columns=[name]
        print 'Here\'s your list of',df

while asking == True:
    add = raw_input('Would you like to add an item? (y/n) ')
    if add == 'y':
        asker()
        break
        
    elif add == 'n':
        print 'Okay cool beans sir'
        asking == False
        break
            
    else:
        print 'go away'
        asking == False
        break
