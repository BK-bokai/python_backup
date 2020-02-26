from source import daily, weekly
print("Daily forecast:", daily.forecast())
print('Weekly forecast:')
for unmber, outlook in enumerate(weekly.forecast(), 1):
    print(unmber, outlook)