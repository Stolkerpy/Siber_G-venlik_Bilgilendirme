print("1-) savunma\n2-) Toollar\n3-) Hackerler ile ilgili bilgilier\n4-) İletişim Discord \n0-) ÇIKIŞ")

giris = int(input("Seçeneği griiniz : "))

if (giris) == 0:
    print("Çıkılıyor...")
    exit()
else:
    print("Yannlış Tuşa Bastın Sanıtım .d")

if (giris) == 1:
    print("*"*30)
    print("Siber Savunma ile ilgili öğrenmek istediğiniz bilgiyi seçiniz")
    giris1 = int(input("1-)tor ile ilgili bilgiler\n2-)kendi siteni nasıl savunursun\n3-)dos ve ddos ataklarına karşı önlemler\n\nÖğrenmek istediğiniz bilginin numarasını giriniz : "))
    if (giris1) == 1:
        print("*"*30)
        print("Tor Browser Nedir? Nasıl Çalışır?\nTor, açılımı “The Onion Routing” olan kullanıcılarının gerçek kimliklerini gizleyerek iletişim imkanı sunan bir yazılım projesidir. Tor yasal ya da yasal olmayan bir çok amaç için kullanılmaktadır. Tor internette gezinme, sohbet ve anlık mesajlaşma imkanı sağlar. Ayrıca tor, devlet yetkililerini eleştirmek, sansürlenmiş bilgilere erişmek ve politik aktiviteler organize etmek amacıyla da kullanılmaktadır. Tor da; anonim hakaret, hassas bilgilerin sızdırılması, yasal olmayan cinsel içeriklerin sunulması, satışı yasak olan kimyasal maddelerin, silahların çalıntı kredi kart numaralarının satılması, banka ve kredi kartı dolandırıcılığı gibi kara borsa işlemleri için BitCoin sistemi kullanılır. Bu projeye göre, Tor ağını kullananlar; bağlandıkları sitelerden aktivitelerini gizlemek isteyen normal kullanıcılar, siber istihbarat faaliyetlerinden kaçan insanlar, içerik veya internet erişimine yapılan sansürden kaçan insanlar özellikle de gazeteciler, aktivistler ve askeri çalışanlardır. Ekim 2013 tarihi itibariyle Tor ağını 4 milyon kişi kullanmaktadır. Tor ağını kullananların büyük kısmı, internet erişiminin engellediği ülkelerde yaşamaktadırlar.")
        print("Tor Projesi’nin Tarihi\nTor Projesi 1995 yılında ABD Deniz Harp Araştırma Laboratuvarı’nda Paul Syverson, Micheal Reed ve David Goldschlog tarafından, gizli servislerin çevrim içi istihbarat bilgilerini koruma amacıyla başlamıştır. Proje askeri ve istihbarat amacıyla başladığı için hedefinde mahremiyet yoktu. Sadece askeri personel ve istihbaratları maskeleme işlemi yapıyordu. Tor projesinde çalışmaların yavaş ilerlemesi sonucunda 2002 yılında Tor projesi MIT’de 2 doktora öğrencisi olan Roger Dingledine ve Nick Mathewson’a devredildi. Daha sonraki yıllarda Paul Syverson ile birlikte bu üçlü Tor projesi üzerinde çalışmışlardır. Çalışmalar ilerlerken bu projenin sadece askeri amaçlı olması ajanları korumanın daha zor olduğu kararını almalarını sağlamıştır. Bu sebeple ağın sadece askeri amaçlı değil daha geniş kitlelerinde bu ağa erişebilmesi yönünde çalışmalara başlamışlardır. İlk olarak Tor projesi Deniz Harp Araştırmaları Laboratuarından ayrılmış, daha sonra herkesin kullanabileceği şekilde tasarlanmıştır. Buradaki amaç kullanıcı sayısını arttırarak gizlenmeyi kolaylaştırmaktır. 2004 yılında Tor, açık kaynak lisanslı hale getirilmiştir. Proje açık kaynak olduğunda EFF (The Electronic Frontier Foundation) bu projeyi devraldı. Tor, ilk zamanlarında askeri bir proje olduğu için yerilmiştir. İleriki yıllarda bu projeye destek artmıştır. Şu anda kurumsal sponsorlar hariç 4300 bireysel sponsor Tor projesine destek vermektedir.")
        print("Tor Çalışma Yapısı\nTor, anonim ağ yapılarından onion routing mantığında çalışır. Tor üzerinden bir internet sitesine istek yolladığında en az 5 server üzerinden istek gönderilir. İstek ilk server tarafından değerlendirilir, sonra ikinci servera iletilir. Daha sonra ikinci server isteği değerlendirir ve bunu üçüncü servera iletir. Tüm bu işlemler istek gönderdiğiniz siteye erişesiye kadar devam eder. Bu işlemler gerçekleşirken bilgileriniz şifrelenir. Her server  Bilgileriniz her server geçişinde şifrelendiğinden ve bağlantı yollarken bir çok server üzerinden geçtiğinizden dolayı hangi bağlantıya giriş yapıldığını öğrenmek neredeyse imkansız olur. Bu da güvenirliliği arttırır. Hız açısından bir çok server yolu üzerinden bağlantı sağladığı için normal google üzerinden bağlantı yapmaktan daha yavaş bir bağlantı hızı sunmaktadır. Tor Browser, mozilla firefox klonudur. Firefox’un açık kaynak bir proje olmasının da katkısıyla NSA monitörlemesinden sizi büyük ölçüde koruyabilmektedir. Tor ağındaki kullanıcılara erişmek çok zor ve zahmetli bir iştir çünkü internet trafiğini 4binden fazla gönüllü server aracılığıyla yansıtarak sizin konumunuzu ve verilerinizi bulunması imkansız hale getirir. isterseniz bu gönüllü hostlardan biri olabilirsiniz.")
        print("Tor %100 Koruma Sağlar Mı?Bu en çok tartışılan sorulardan biridir. Teknik olarak düşünüldüğü zaman %100 koruma sağlandığı söylenemez. Derinlemesine bir network takibi yapıldığında, network izleri dijital ortamda yakalanabilir. Tor sadece farklı serverlara şifreli bağlantı sağlayarak internette gezinmenizin izlenmesini zorlaştırır.")
        print("Tor Browser Nasıl İndirebilirim?\nTor Browser’ı kendi sitesinden indirebileceğiniz gibi, Mozilla Firefox’a eklenti şeklinde de kurabilirsiniz.")
    elif (giris1) == 2:
        print("*"*30)
        print("İşletmelerin korkulu rüyası haline gelen siber saldırılara karşı nasıl önlemler alınmalı\nGünümüz teknoloji devri , her ne kadar işletmemizin bir çok alanda işlerini kolaylaştırp zaman ve para tasarrufu yapıyorsa bir o kadar da güvenlik zafiyetleri oluşturmakta. Bir tıkla hayatımızı ve özellikle verilerin depolanmasında büyük fayda sağlayan bu teknoloji güvenlik zafiyetleri sonucu siber saldırılara uğradığında büyük maddi zararlara yol açmaktadır.Peki Siber saldırılardan korunmak için ne yapmalı ?Şirket çalışnaları mutlaka bilinçlendirilmeli")
        print("Şirket için önemli e-postalar ve bilgilerin depolanması ve korunmasında elbette şirket çalışanlarının bilinçlendirilmesi çok çok önemlidir. Şirketin bir güvenlik politikası oluşturulmalı sürekli eğitimler verilmeli ayrıca yeni katılan personele oryantasyon dahilinde bu güvenlik politikları benimsetilmelidir.Şifre Güvenliği ve ÖnemiAraştırmalar gösteriyor ki yapılan bu saldırıların büyük çoğunluğu kimlik hırsızlığı yöntemleri ile geçekleşiyor. Yani sisteme dahil olan bir kullanıcının bilgileri (şifresi) ele geçiriliyor ve bununla sistemin içine giriliyor. Ön saldırı sistem içnden birinin kimlik bilgileri ele geçirmek ile başlıyor.Kullanıcıların şifre güvenliği bu işin başı olmakta. Peki Hayaıtı önem taşıyan bu şifreler nasıl olmalı ;Öncelikle her şifre kişiye ve sistme özel olmalı ve sadece yetkili kişilerce bilinmeli")
        print("Tahmini kolay şifreler olmamalı 123.. veya abc , qwer gibi şifreler hem harf hem rakam hemde ASCI karekter içermeli ($,?,* gibi )Oltalama Saldırılarına Dikkat Şirket çalışanlarının en çok dikkat etmesi gereken bir konuda oltalama diye tabir edilen resmi kurum , banka , internet servis sağlayı , Faturalama servisleri , Kargo vs isimleri kullanarak gönderilen mailler. Bir dalgınlıkla açılan bu mailler sisteme geri dönülemez hasarlar vermektedir.Bir çok yazılımda ve antivirus paketlerinde bulunan gelişmiş tehdit koruması işe yarasada %100 engelmek mümkün değildir. Yine burda şirketin Güvenlik politikası ve çalışanlara verdiği eğitim öne çıkmaktadır.Anti Virüs Şart Ama Yeterli DeğilSiber saldırılara karşı alınacak en büyük önemler lisanlı bir işletim sistemi ve lisanslı bir antivirüs kullanmaktır. Ancak günümüzde gelişmiş siber saldırılara karşı antivirüs programları yetersiz kalabilir. Araştırmalar küçük ve orta işletmeleirnin 5 te 1 bu tür saldırılara maruz kaldığını ve çalınan verileri ortalama 200 gün sonra fark edebildiğini tesbit etmiştir.Daha Güvenli sistemler için Lisanslı Antivirüs ve İşletim sistemelri ve yedeklemenin önemi bir kez daha ortaya çıkmaktadır.")
    elif (giris1) == 3:
        print("*"*30)
        print("\n\nYazılım geliştiricileri için web tabanlı bir depolama servisi sunan GitHub, geçtiğimiz hafta internet tarihinin en büyük DDoS salıdırısına uğradı. Saniyede 1,35 terabitlik veri akışıyla yoğun saldırıya maruz kalarak dakikalarca hizmet veremeyen site saldırıya yapılan müdahalelerin ardından normale döndü. GitHub gibi önemli bir site dahi DDoS saldırılarını yardım alarak atlatabilirken, şirketler bu saldırılara karşı nasıl önlem alabilir? Lider güvenlik duvarı ve UTM sağlayıcısı WatchGuard, DDoS saldırılarının nasıl önleneceğine ve azaltılacağına dair önerilerde bulunuyor. Kullanıcıların internet erişimlerini engellemek için genellikle siber suçlular DDoS saldırılarını kullanıyor. Bu saldırılar, siteleri yoğun trafiğe maruz bırakarak geçici olarak çevrimdışı bırakıyor ve sunucularla erişimi kesiyor. 28 Şubat’ta gerçekleşen bu saldırıyı fark eden GitHub yöneticileri ve yazılımcıları, kötü niyetli istekleri engelleyerek bu tür olayları hafifleten Akamai Prolexic’ten yardım istediler. Şirket, birkaç dakika içinde GitHub'ı tekrar çevrimiçi duruma getirmeyi başardı. Bu saldırıyı diğer saldırılardan farklılaştıran ise genellikle DDoS olaylarında kullanılan botnetlerin bu saldırıda kullanılmamasıydı. Siber suçlular, farklı bir yol izleyerek GitHub'un IP adresini sızdırdılar ve genelde veri tabanı odaklı siteleri daha hızlı hale getirmek için kullanılan Memcached sunuculara sorgular gönderdiler. Sunucular daha sonra bu isteklerin verilerini GitHub'a ")
        print("yönlendirdi ve veri akışı bir anda 50 kat artarak saniyede 1,35 terabite ulaştı. DDoS Saldırılarından Korunmak İçin Neler Yapmalısınız? Şirket ağlarına yönelik benzer saldırılara karşı uyaran dünyanın önde gelen güvenlik duvarı ve UTM sağlayıcısı WatchGuard, IT yöneticilerinin bu riskleri en aza indirmeleri için gerekli planlamayı yapmaları gerektiğini belirterek DDoS saldırılarını önlemeye ya da azaltmaya yönelik önerilerde bulunuyor. Şirket içi güvenlik duvarlarından veya içerik filtrelerinden yararlanma: WatchGuard Güvenlik Duvarları, cihazdaki varsayılan paket kullanımı yoluyla gönderenin IP adresini engelleyebiliyor. Firebox, hem istemci hem de sunucular için varsayılan eşik değerlerine sahip. Hedef IP adresi için bir eşiğe ulaşıldığında, Firebox herhangi bir ana bilgisayardan gelen bağlantı isteklerini azaltıyor. Ayrıca WatchGuard, 11211 numaralı bağlantı noktasını engelleyerek sunucuların yansıtıcı haline gelmesini önlüyor. Özelleştirilmiş ekipman ve yük dengesi: ISP bağlantılarınız için bir yük dengeleme çözümü uygulayabilirsiniz. Böylece trafik, dairesel denetim ya da taşma senaryolarında kullanılabilir. Genellikle Ağ Boarderlarındaki yükü idare etmek için çeşitli ekipmanlar kullanılır. Bu cihazların hacimsel/volümetrik saldırılarla (bu tür amplifikasyon saldırıları gibi yüksek trafiğe sahip saldırılar) mücadele edemeyeceği/önleyemeyeceği konusunda dikkatli olun. Bu saldırılar ağ üzerinde tıkanma/engel oluşturacaktır. ISP ve 3. partilerin hafifletilmesi: ")
        print("Bu önlemler genellikle bir arada ele alınır. Büyük ölçekli saldırılar için, ISP ve üçüncü parti bir bulut hafifletme servisinin koordinasyonuna bağımlı olmanız gerekir")

elif (giris) ==2:
    print("*"*30)

    giris2 = int(input("1-) DDOS Tool\n2-) açık tarama\n3-) Sosyal Mühendislik Tooları\n\nİstediğiniz Toolun Numarasını giriniz : "))
    
    if (giris2) == 1:
        print("Dos ve DDOS için en iyi sc ler https://github.com/COLAK-C/DDoS-Tools")
    if (giris2) == 2:
        print("En iyi açık Tarama sc leri \n https://github.com/poerschke/Uniscan\n https://github.com/praharshjain/port-scanner \n https://github.com/1N3/Sn1per")
    if (giris2) == 3:
        print("En iyi Sm Sc leri \n https://github.com/Screetsec/TheFatRat \n https://github.com/DarkSecDevelopers/HiddenEye")
elif (giris) == 3:
    print("*"*30)
    print("Hacker ne demek?\n\nŞahsî bilgisayarlara veya çeşitli kurum ve kuruluşlara ait bilgisayarlara ve ağlara izinsiz olarak giriş yapan kişi. Daha geniş ve tarihsel bir ifade ile, elektronik veya mekanik otomat sistemlerine girilmesi gereken bilgi, jeton gibi doğru anahtarın kullanıldığını kontrol eden anahtar yuvası olan filtreyi kopya anahtarlar ile geçerek hizmet verici sistemi yanıltan kişi.Bilgisayar programcılığı alanında, bir hacker bir exploit'e bir dizi düzeltme uygulama ya da varolan kodları kullanma yoluyla bir amaca ulaşan ya da onu 'kıran' bir programcıdır.İLGİLİ SON HABERVeri tabanına sızıp üniversiteli oldular")
    print("\n\nHacker türleri\n\n Öncelikle Hack.. Hack sözcüğünün kelime karşılığı ”kırmak, kıymak ve kesmek” anlamlarındandır. Dolayısıyla bir yazılımı veya bilgiyi çözenlere, kıranlara Hacker denir. Hacker’lar genel tanı itibari ile kötü gösterilirler ve bilgilerinin dar olduğuna inanılır, ama bu yanlış bir tanıdır. Her Hacker kötü olmadığı gibi her Hacker’da bilgisiz değildir. Hatta gerçek bir Hacker bir yazılımcıdan (Hani şu bir suru programlama dili bilenlerden) daha da bilgilidir. Hacker, programlama dillerinin yanı sıra network, OS, donanım, sistem mimarisi gibi bir çok alanda bilgi sahibidir.\n\n Haberlere yansıyan bilgilere baktığımızda Hackerlar ya bir yeri soyar veya bir bilgiyi çalarlar, ama bu genel bir anlam ifade etmez. Elinde silah olan her insan nasıl kötü değilse her Hacker da kötü değildir. Şimdi Hacker tanımını yapmak gerekirse; Hacker, bir bir sistemin veya yazılımın açığını bulabilen kişidir. Bu kadar Hacker dedik gelin şimdide Hackerların türlerine bir bakalım. (Kim bilir belki sizde bir Hacker türündensiniz)")
    print("\n\nHacktivist\n\n Bu grupta yer alan Hackerların bir amacı ve ideolojisi vardır. Genel anlamda görüşleri ”Bilgi herkesindirve kamusal olmalıdır” çevresinde şekillenir. Kendilerine göre yanlış buldukları bir politik olayı veya toplumsal olayı düzeltmeye çalışırlar. Bunu da genelde siteleri Hackleyip site üzerinde mesaj vererek yaparlar.")
    print("\n\nBlack Hat; (Siyah Şapkalılar)\n\n Hacker türleri arasındaki en zararlı ve aynı zamanda en çok bilgi sahibi olanlardır. Hedefleri her türlü bilgisayarı, sistemi, yazılımı, siteyi Hacklemektir ki bunu da çoğu zaman gerçekleştirirler. Girdikleri sistemi bozabilirler, tüm bilgileri alabilirler ve bilgiler sayesinde maddi kazanç sağlayabilirler.")
    print("\n\nWhite Hat; (Beyaz Şapkalılar)\n\n Beyaz Şapkalılar Hacker türleri arasında babacan adamlardır. Zarar vermeyi gütmezler ama Siyah Şapkalılar kadar bilgilidirler. Zaten hayatlarını da böyle kazanırlar, bazıları şirketlerde veya devlet kurumlarında çalışırlar. Amaçları Siyah Şapkalıları önlemek, verdikleri zararları gidermektir. (İlla Hacker olacam falan diyorsanız bunu olun, babacan olun)")
    print("\n\nGrey Hat; (Gri Şapkalılar)\n\n Bu kişiler arasında hem Beyaz hemde Siyah şapkalılar olabilir, daha doğrusu onların yaptıklarını yapabilirler. Bu yüzden iyi niyetli olup olmadıklarını anlayamayız. Genelde sistem açıklarını bulup içeriye şöyle bir bakarlar ancak ”genelde” bilgi çalmazlar. Sonrasında ise açığı para karşılığında sistem yöneticisine bildirirler veya bazen açıkları rakip sistemlere bildirirler.")
    print("\n\nCracker; (Yazılım Korsanları)\n\n Bunları biliyorsunuz zaten 😀 Korsan oyunlar, yazılımları bunlar hazırlar. Lisanlı yazılımların kodlarını baştan derleyebilirler veya hiç uğraşmaz aktivatör yaparlar. Örneğin Windows 8’i tam sürüm yapma aracı gibi, veya Pes 2013’ün crack’ı gibi. Gözünüze iyi gibi görünseler de kötüdürler, korsan kullanmayın. Yaptıkları yazılımların içine virüs veya botnet koyabilirler, sonra bilgisayarım niye zombi oldu demeyin.")
    print("\n\nPhreaker;\n\n Genelde hedeflerini çok büyük tutmazlar. Telefon ağlarını, Uluslararası Ağları veya VoIP ağları hackerler ve bedava görüşme gibi birkaç iş yaparlar. Veya konuşmalarınızı dinleyebilirler ve bilgileri satabilirler.")
    print("\n\nLamer;\n\n Bu kişilere Hacker demek Hackerlara hakarettir (Hackerlara hakaret etmeyin, Hacklerler) ama isimleri yine de Hacker türlerinde geçer. Bilgi dereceleri SIFIRDIR ve sağda solda buldukları bir iki bilgiyle – bunların ne olduklarını bilmeseler bile – övünürler. Bazı sitelerde ”Lamer’lar Giremez” diye başlıklar bile açılır. Bana Trolleri anımsatıyorlar.")
    print("\n\nScript Kiddie;\n\n Lamer’ların bir tık üstü. Genelde lise öğrencileri olan bu grup bilgisayara aşırı meraklıdır ve Hackerlara karşı aşırı sevgi gösterirler ayrıca onlar gibi olmak isterler. Araştırıp bilgi edinirler ve edindikleri bilgileri zararlı amaçlar için kullanırlar. Amatör anarşistler olarakda bazı yerlerde geçerler çünkü kendilerinin Hacker olduklarını söylemekten çekinmezler.")
    print("\n\nPentester\n\n Penetration Testing  ?Sistemi dışarından gelecek saldırları ekstra bilgi sahibi olmadan güvenlik açıklarına karşı test etmek ve bu açıkları mümkün olduğu kadar exploit etmek.Günümüzde bu degişerek az bir bilgi vererekte pentest çalışması yapılmaktadır.Bunu söylemeden geçmek istemedim.Pentest çalışmaları aslında hemen hemen her şirketin yaptırması gerekir tabi güvende olmak ve güvende kalmak,sorun yaşamak istemiyorlarsa.Pentester,Penetration testing çalışmaları yapan kişidir.Pentester, Dışarıdan saldırı düzenleyerek sistemi exploit etmeye çalışır.Pentester,bir hacker gibi düşünüp hatta daha fazlasını düşünüp web siteye saldırı düzenlemek zorundadır çünkü başka türlü güvenligini saglayamaz.Pentester bir çok bilgiyi bilen bunların başında linux gibi açık kaynak kodları ,programlama bilgisi (python)ve daha fazlasını bilir ve bilmek zorundadır.")
if (giris) == 4:
    print("*"*30)
    print("HUN HACK TEAM\nEğer Aslanlar Gelirse Sonuna Kadar Savaşacağız !\nEğer Kaplanlar Gelirse  Savaşacağız !\nEğer İnsanlar Gelirse Öfke İle Savaşacağız !\nEĞER HUN GERİ DÖNERSE BİZ YOK EDECEĞİZ.! ")
    print("\n\nDiscord : https://discord.gg/BcXgD55")
    print("\n\n☣𐰚𐰇𐰠𐰍𐰇∶𐰴𐰣-Hülâgû Han-𐰚𐰇𐰠𐰍𐰇∶𐰴𐰣☣#4151")
    

