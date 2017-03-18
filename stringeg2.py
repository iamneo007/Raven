s = input('enter the string:')

#count the naumber of vowels
print("No. of 'a' = %s" % s.count("a"))
print("No. of 'e' = %s" % s.count("e"))
print("No. of 'i' = %s" % s.count("i"))
print("No. of 'o' = %s" % s.count("o"))
print("No. of 'u' = %s" % s.count("u"))

#calculatet percentage of vowels
total_vowels = s.count('a') + s.count('e') + s.count('i') + s.count ('o') + s.count('u')
percentage = (float(total_vowels)) / len(s) * 100
print("\n%.2f%% are vowels." % percentage)