#s24016
#関数で消費税10%を計算するプログラム

def postTaxPrice(price):
    ans=price*1.1
    return int(ans)

print(postTaxPrice(120),"円")
print(postTaxPrice(128),"円")
print(postTaxPrice(980),"円")
