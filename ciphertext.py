giventext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
result = ""
for i in giventext:
    if i.isalpha():
        if i.isupper():
            k = ord(i)
            q=k-13
            if q<65:
                q=q+26   
            text = chr(q)
        else:
            k = ord(i)
            q=k-13
            if q<97:
                q=q+26
            text=chr(q)
    else:
        text = i
    result += text
print(result)
