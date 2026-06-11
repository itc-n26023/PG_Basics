words=["The","fox","jumped","over","the","fence","."]

#(" ")を使ってに連結する
full_sentence=" ".join(words)

#print文で表示
#[0:-2]で先頭(0)から最後から二個手前(-2)までをカットし、最後に文字列の足し算(=".")でピリオドをくっつける
print(full_sentence[0:-2]+".")
