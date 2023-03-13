import random
import regex as re

uniChars = "àáảãạâầấẩẫậăằắẳẵặèéẻẽẹêềếểễệđìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵÀÁẢÃẠÂẦẤẨẪẬĂẰẮẲẴẶÈÉẺẼẸÊỀẾỂỄỆĐÌÍỈĨỊÒÓỎÕỌÔỒỐỔỖỘƠỜỚỞỠỢÙÚỦŨỤƯỪỨỬỮỰỲÝỶỸỴÂĂĐÔƠƯ"
unsignChars = "aaaaaaaaaaaaaaaaaeeeeeeeeeeediiiiiooooooooooooooooouuuuuuuuuuuyyyyyAAAAAAAAAAAAAAAAAEEEEEEEEEEEDIIIOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYAADOOU"

def loaddicchar():
    dic = {}
    char1252 = 'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ'.split(
        '|')
    charutf8 = "à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ".split(
        '|')
    for i in range(len(char1252)):
        dic[char1252[i]] = charutf8[i]
    return dic

dicchar = loaddicchar()

def convert_unicode(txt):
    return re.sub(
        r'à|á|ả|ã|ạ|ầ|ấ|ẩ|ẫ|ậ|ằ|ắ|ẳ|ẵ|ặ|è|é|ẻ|ẽ|ẹ|ề|ế|ể|ễ|ệ|ì|í|ỉ|ĩ|ị|ò|ó|ỏ|õ|ọ|ồ|ố|ổ|ỗ|ộ|ờ|ớ|ở|ỡ|ợ|ù|ú|ủ|ũ|ụ|ừ|ứ|ử|ữ|ự|ỳ|ý|ỷ|ỹ|ỵ|À|Á|Ả|Ã|Ạ|Ầ|Ấ|Ẩ|Ẫ|Ậ|Ằ|Ắ|Ẳ|Ẵ|Ặ|È|É|Ẻ|Ẽ|Ẹ|Ề|Ế|Ể|Ễ|Ệ|Ì|Í|Ỉ|Ĩ|Ị|Ò|Ó|Ỏ|Õ|Ọ|Ồ|Ố|Ổ|Ỗ|Ộ|Ờ|Ớ|Ở|Ỡ|Ợ|Ù|Ú|Ủ|Ũ|Ụ|Ừ|Ứ|Ử|Ữ|Ự|Ỳ|Ý|Ỷ|Ỹ|Ỵ',
        lambda x: dicchar[x.group()], txt)

bang_nguyen_am = [['ả', 'ã', 'á', 'à', 'ạ', 'a', 'a'],
                  ['ẳ', 'ẵ', 'ắ', 'ằ', 'ặ', 'ă','aw'],
                  ['ẩ', 'ẫ', 'ấ', 'ầ', 'ậ', 'â', 'aa'],
                  ['ẻ', 'ẽ', 'é', 'è', 'ẹ', 'e', 'e'],
                  ['ể', 'ễ', 'ế', 'ề', 'ệ', 'ê', 'ee'],
                  ['ỉ', 'ĩ', 'í', 'ì', 'ị', 'i', 'i'],
                  ['ỏ', 'õ', 'ó', 'ò', 'ọ', 'o', 'o'],
                  ['ổ', 'ỗ', 'ố', 'ồ', 'ộ', 'ô', 'oo'],
                  ['ở', 'ỡ', 'ớ', 'ờ', 'ợ', 'ơ', 'ow'],
                  ['ủ', 'ũ', 'ú', 'ù', 'ụ', 'u', 'u'],
                  ['ử', 'ữ', 'ứ', 'ừ', 'ự', 'ư', 'uw'],
                  ['ỷ', 'ỹ', 'ý', 'ỳ', 'ỵ', 'y', 'y'],
                  ['Ả', 'Ã', 'Á', 'À', 'Ạ', 'A', 'A' ],
                  ['Ẳ', 'Ẵ', 'Ắ', 'Ằ', 'Ặ', 'Ă', 'AW'],
                  ['Ẩ', 'Ẫ', 'Ấ', 'Ầ', 'Ậ', 'Â', 'AA'],
                  ['Ẻ', 'Ẽ', 'É', 'È', 'Ẹ', 'E', 'E'],
                  ['Ể', 'Ễ', 'Ế', 'Ề', 'Ệ', 'Ê', 'EE'],
                  ['Ỉ', 'Ĩ', 'Í', 'Ì', 'Ị', 'I', 'I'],
                  ['Ỏ', 'Õ', 'Ó', 'Ò', 'Ọ', 'O', 'O'],
                  ['Ổ', 'Ỗ', 'Ố', 'Ồ', 'Ộ', 'Ô', 'OO'],
                  ['Ở', 'Ỡ', 'Ớ', 'Ờ', 'Ợ', 'Ơ', 'OW'],
                  ['Ủ', 'Ũ', 'Ú', 'Ù', 'Ụ', 'U', 'U'],
                  ['Ử', 'Ữ', 'Ứ', 'Ừ', 'Ự', 'Ư', 'UW'],
                  ['Ỷ', 'Ỹ', 'Ý', 'Ỳ', 'Ỵ', 'Y', 'Y'], 
                  ]
bang_ky_tu_dau = ['r', 'x', 's', 'f', 'j', '',]

nguyen_am_to_ids = {}
phu_am_ids = {}
nguyen_am_ids = {}

for i in range(len(bang_nguyen_am)):
    for j in range(len(bang_nguyen_am[i]) - 1):
        nguyen_am_to_ids[bang_nguyen_am[i][j]] = (i, j)

M82charPA =[['B', 'Ký tên', 'T', 'S', 'R', 'Q', 'Tr', 'Gi','Báo cáo', '10'],
            ['1','C','V','W','F', 'P','Qu', 'Ng', 'Kính gửi','11'],
            ['6','2','D','X','Z','N','Ch','Ngh',' ', 'Phụ lục 3'],
            ['Ngày','7','3','Đ','Y','M','Th','Gh', 'Phụ lục 1','12'],
            ['Tháng', '8','4','G','J','L','Kh','Ph',' ', 'Phụ lục 4'],
            ['Năm','9','5','0','H','K','Nh', ' ','Phụ lục 2','13']
           ]

M82charNA = [['a','anh', 'ôc', 'oai','uât','uây','uyt','eng', ' ', '14'],
             ['ă','ang','ơc','oi','ưu','ua','ươn','êng','iêm','15'],
             ['â','ăng','ot','ôi','uôi','ưa','ui','ênh','iêu','16'],
             ['an','âng','ôt','ơi','ươc','uyêt','ưi','êch','ich','17'],
             ['ăn','ap','ơt','oe','uơc','uêch','ươu',' ','  ','18'],
             ['ân','ăp','op','oach','ung','uênh',' ','i','  ','19'],
             ['am','âp','ôp','oong','uynh','ương','e','it','yêt','20'],
             ['ăm','ay','ơp','ooc','uyn','uông','ê','in','yêu','21'],
             ['âm','ây','oat','oang','uyu',' ','en','im','yên','22'],
             ['au',' ','oăt','ong','uê','um','ên','ip',';','23'],
             ['âu','o','oen','ông','ươp','ưm','em','iu','/','24'],
             ['ai','ô','oam','oay','uych','un','êm','ia','-','25'],
             ['ao','ơ','oan',' ','uôt','ưn','et','inh','=','26'],
             ['ac','on','oăn','u','uy','ưng','êt','ing','?','27'],
             ['ăc','ôn','oanh','ư','up','uya','ep',' ','%','28'],
             ['âc','ơn','oap','ut','ưp','ươm','êp','iêng','Giờ','29'],
             ['at','om','oăc','ưt','uân','uôm','ec','iêp','…','30'],
             ['ăt','ôm','oa','uc','uâng','uen','êc','iêc','00','31'],
             ['ât','ơm','oet','ưc','ươi','uôn','êu','iêt','000',':'],
             ['ach','oc','oac','ươn','ưt','uyên','eo','iên','<....>','.']
]
M82dau = [['0' ,'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9'],
          ['8' ,'9' ,'0' ,'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7'],
          ['6' ,'7' ,'8' ,'9' ,'0' ,'1' ,'2' ,'3' ,'4' ,'5'],
          ['4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'0' ,'1' ,'2' ,'3'],
          ['2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'0' ,'1']
          ]
M82numPA = [['7' ,'5' ,'3' ,'1' ,'9'],
            ['8' ,'6' ,'4' ,'2' ,'0'],
            ['9' ,'7' ,'5' ,'3' ,'1'],
            ['0' ,'8' ,'6' ,'4' ,'2'],
            ['1' ,'9' ,'7' ,'5' ,'3'],
            ['2' ,'0' ,'8' ,'6' ,'4']
            ]
M82numNA = [['78' ,'34' ,'07' ,'63' ,'29'],
            ['79' ,'35' ,'08' ,'64' ,'20'],
            ['70' ,'36' ,'09' ,'65' ,'21'],
            ['71' ,'37' ,'00' ,'66' ,'22'],
            ['72' ,'38' ,'01' ,'67' ,'23'],
            ['73' ,'39' ,'02' ,'68' ,'24'],
            ['74' ,'30' ,'03' ,'69' ,'25'],
            ['75' ,'31' ,'04' ,'60' ,'26'],
            ['76' ,'32' ,'05' ,'61' ,'27'],
            ['77' ,'33' ,'06' ,'62' ,'28'],
            ['90' ,'56' ,'11' ,'85' ,'41'],
            ['91' ,'57' ,'12' ,'86' ,'42'],
            ['92' ,'58' ,'13' ,'87' ,'43'],
            ['93' ,'59' ,'14' ,'88' ,'44'],
            ['94' ,'50' ,'15' ,'89' ,'45'],
            ['95' ,'51' ,'16' ,'80' ,'46'],
            ['96' ,'52' ,'17' ,'81' ,'47'],
            ['97' ,'53' ,'18' ,'82' ,'48'],
            ['98' ,'54' ,'19' ,'83' ,'49'],
            ['99' ,'55' ,'10' ,'84' ,'40'],
]

specPA = {'ký': 'tên',
          'báo' : 'cáo',
          'kính' : 'gửi',
          'phụ' : 'lục' ,
          'ngày' : 1,
          'tháng' : 1,
          'năm' : 1
        }
PLnum = ['1','2','3','4']
for i in range(len(M82charNA)):
    for j in range(len(M82charNA[i])):
        M82charNA[i][j] = M82charNA[i][j].lower()
        nguyen_am_ids[M82charNA[i][j]] = (i, j)
        
for i in range(len(M82charPA)):
    for j in range(len(M82charPA[i])):
        M82charPA[i][j] = M82charPA[i][j].lower()
        phu_am_ids[M82charPA[i][j]] = (i, j)  

def vn_word_to_telex_type(word):
    dau_cau = 0
    new_word = ''
    for char in word:
        x, y = nguyen_am_to_ids.get(char, (-1, -1))
        if x == -1:
            new_word += char
            continue
        if y != 0:
            dau_cau = y
        new_word += bang_nguyen_am[x][-1]
    new_word += bang_ky_tu_dau[dau_cau]
    return new_word


def vn_sentence_to_telex_type(sentence):

    words = sentence.split()
    for index, word in enumerate(words):
        words[index] = vn_word_to_telex_type(word)
    return ' '.join(words)


def chuan_hoa_dau_tu_tieng_viet(word):
    if not is_valid_vietnam_word(word):
        return word
        
    chars = list(word)
    dau_cau = 5
    nguyen_am_index = []
    qu_or_gi = False
    for index, char in enumerate(chars):
        x, y = nguyen_am_to_ids.get(char, (-1, -1))
        if x == -1:
            continue
        elif x == 9 or x == 21:  # check qu
            if index != 0 and chars[index - 1] == 'q':
                chars[index] = 'u'
                qu_or_gi = True
        elif x == 5 or x == 17:  # check gi
            if index != 0 and chars[index - 1] == 'g':
                chars[index] = 'i'
                qu_or_gi = True
        if y != 5:
            dau_cau = y
            chars[index] = bang_nguyen_am[x][5]
        if not qu_or_gi or index != 1:
            nguyen_am_index.append(index)
    if len(nguyen_am_index) < 2:
        if qu_or_gi:
            if len(chars) == 2:
                x, y = nguyen_am_to_ids.get(chars[1])
                chars[1] = bang_nguyen_am[x][dau_cau]
            else:
                x, y = nguyen_am_to_ids.get(chars[2], (-1, -1))
                if x != -1:
                    chars[2] = bang_nguyen_am[x][dau_cau]
                else:
                    chars[1] = bang_nguyen_am[5][dau_cau] if chars[1] == 'i' else bang_nguyen_am[9][dau_cau]
            return ''.join(chars)
        return word

    for index in nguyen_am_index:
        x, y = nguyen_am_to_ids[chars[index]]
        if x == 4 or x == 8 or x == 16 or x == 20:  # ê, ơ
            chars[index] = bang_nguyen_am[x][dau_cau]
            # for index2 in nguyen_am_index:
            #     if index2 != index:
            #         x, y = nguyen_am_to_ids[chars[index]]
            #         chars[index2] = bang_nguyen_am[x][0]
            return ''.join(chars)
    
    if len(nguyen_am_index) == 2:
        if nguyen_am_index[-1] == len(chars) - 1:
            x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
            chars[nguyen_am_index[0]] = bang_nguyen_am[x][dau_cau]
            # x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
            # chars[nguyen_am_index[1]] = bang_nguyen_am[x][0]
        else:
            # x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
            # chars[nguyen_am_index[0]] = bang_nguyen_am[x][0]
            x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
            chars[nguyen_am_index[1]] = bang_nguyen_am[x][dau_cau]
    else:
        # x, y = nguyen_am_to_ids[chars[nguyen_am_index[0]]]
        # chars[nguyen_am_index[0]] = bang_nguyen_am[x][0]
        x, y = nguyen_am_to_ids[chars[nguyen_am_index[1]]]
        chars[nguyen_am_index[1]] = bang_nguyen_am[x][dau_cau]
        # x, y = nguyen_am_to_ids[chars[nguyen_am_index[2]]]
        # chars[nguyen_am_index[2]] = bang_nguyen_am[x][0]
    return ''.join(chars)

def is_valid_vietnam_word(word):
    chars = list(word)
    nguyen_am_index = -1
    for index, char in enumerate(chars):
        x, y = nguyen_am_to_ids.get(char, (-1, -1))
        if x != -1:
            if nguyen_am_index == -1:
                nguyen_am_index = index
            else:
                if index - nguyen_am_index != 1:
                    return False
                nguyen_am_index = index
    return True

def chuan_hoa_dau_cau_tieng_viet(sentence):
    """
        Chuyển câu tiếng việt về chuẩn gõ dấu kiểu cũ.
        :param sentence:
        :return:
        """
    #sentence = sentence.lower()
    words = sentence.split()
    for index, word in enumerate(words):
        cw = re.sub(r'(^\p{P}*)([p{L}.]*\p{L}+)(\p{P}*$)', r'\1/\2/\3', word).split('/')
        #print(cw)
        if len(cw) == 3:
            cw[1] = chuan_hoa_dau_tu_tieng_viet(cw[1])
        words[index] = ''.join(cw)
    return ' '.join(words)


"""
    End section: Chuyển câu văn về cách gõ dấu kiểu cũ: dùng òa úy thay oà uý
    Xem tại đây: https://vi.wikipedia.org/wiki/Quy_tắc_đặt_dấu_thanh_trong_chữ_quốc_ngữ
"""

def DecodeN (number): 
    numbers = []
    for i in range(5):
        if i == 2:
            numbers.append(number[i]+number[i+1])
            continue
        elif i == 3:
            continue
        numbers.append(number[i])
    NA_y = -1
    NA_x = 0
    while (NA_y == -1):
        if  M82numNA[NA_x].count(numbers[2]) != 0:
            NA_y = M82numNA[NA_x].index(numbers[2])
            continue
        NA_x = NA_x + 1
    PA_x = 0
    PA_y = -1
    while (PA_y == -1):
        if M82numPA[PA_x].count(numbers[0]) != 0:
            if M82numPA[PA_x].index(numbers[0]) == NA_y:
                PA_y = NA_y
                continue
        PA_x = PA_x+1
    CharNA = list(M82charNA[NA_x][M82dau[PA_y].index(numbers[3])])
    #print(CharNA)
    x , y = nguyen_am_to_ids.get(CharNA[0],(-1,-1))
    if CharNA[0] == ' ' or CharNA[0] == '  ':
        wordX = M82charPA[PA_x][M82dau[PA_y].index(numbers[1])]
        listwordX = list(wordX)
        if wordX == 'gi':
            listwordX[1] = bang_nguyen_am[5][PA_y+1]
            wordX = ''.join(listwordX)
            wordX = wordX.lstrip()
            if PA_y == 0:
                listwordX[1] = bang_nguyen_am[5][PA_y]
                word2 = ''.join(listwordX)
                word2 = word2.lstrip()
                wordX = wordX.capitalize() + ' (' + word2.capitalize() + ')'
                return wordX
        elif wordX == 'qu': 
            listwordX[1] = bang_nguyen_am[9][PA_y+1]
            wordX = ''.join(listwordX)
            wordX = wordX.lstrip()
            if PA_y == 0:
                listwordX[1] = bang_nguyen_am[9][PA_y]
                word2 = ''.join(listwordX)
                word2 = word2.lstrip()
                wordX = wordX.capitalize() + ' (' + word2.capitalize() + ')' 
                return wordX    
        else:
            wordX = wordX.lstrip() 
            return wordX.capitalize()
    else:
        if PA_y == 0:
            CharNA[0] = bang_nguyen_am[x][PA_y]     
            wordX = M82charPA[PA_x][M82dau[PA_y].index(numbers[1])] + ''.join(CharNA)
            wordX = chuan_hoa_dau_tu_tieng_viet(wordX)
            wordX = wordX.lstrip()
            CharNA[0] = bang_nguyen_am[x][PA_y+1]
            word2 = M82charPA[PA_x][M82dau[PA_y].index(numbers[1])] + ''.join(CharNA)
            word2 = chuan_hoa_dau_tu_tieng_viet(word2)
            word2 = word2.lstrip()
            wordX = wordX.capitalize() + ' (' + word2.capitalize() + ')'
        else:
            if x != -1:
                CharNA[0] = bang_nguyen_am[x][PA_y+1]
            wordX = M82charPA[PA_x][M82dau[PA_y].index(numbers[1])] + ''.join(CharNA)
            wordX = chuan_hoa_dau_tu_tieng_viet(wordX)
            wordX = wordX.lstrip()
            wordX = wordX.capitalize()      
    return wordX

def DecodeNs(numbers):
    number = numbers.split()
    result = []
    for i in range(len(number)):
        result.append(DecodeN(number[i]))
    return ' '.join(result)

def EncodeW(word, checkint):
    dau_cau = 5
    index = 0
    word = word.lower()
    if checkint != 1:
        PAchar = ''
        NAchar = ''
        wordlist = list(word)
        for i in range(len(word)):
            x, y = nguyen_am_to_ids.get(wordlist[i], (-1, -1))
            if y != 5 and y != -1:
                dau_cau = y
            if x != -1: wordlist[i] = bang_nguyen_am[x][5]
        try:
            if wordlist[0] == 'q' and wordlist[1] in bang_nguyen_am[9]:
                if random.choice([1,2]) == 1: 
                    PAchar = PAchar + ''.join(wordlist[0])
                    index += 1
                    NAchar = ''.join(wordlist[(index):])
                    a, b = nguyen_am_ids.get(NAchar, (-1, -1))
                    if a == -1:
                        PAchar = PAchar + ''.join(wordlist[1])
                        index += 1  
                    NAchar = ''.join(wordlist[(index):])
                else:
                    PAchar = PAchar + ''.join(wordlist[0]) + ''.join(wordlist[1])  
                    index += 2
                    NAchar = ''.join(wordlist[(index):])
                    #print(PAchar, NAchar, dau_cau)
            elif wordlist[0] == 'g' and wordlist[1] in bang_nguyen_am[5]:
                if random.choice([1,2]) == 1: 
                    PAchar = PAchar + ''.join(wordlist[0])
                    index += 1
                    NAchar = ''.join(wordlist[(index):])
                    a, b = nguyen_am_ids.get(NAchar, (-1, -1))
                    if a == -1:
                        PAchar = PAchar + ''.join(wordlist[1])
                        index += 1  
                    NAchar = ''.join(wordlist[(index):])
                else:
                    PAchar = PAchar + ''.join(wordlist[0]) + ''.join(wordlist[1])
                    index += 2
                    NAchar = ''.join(wordlist[(index):])
            else:
                for i in range(len(word)):
                    x, y = nguyen_am_to_ids.get(wordlist[i], (-1, -1))
                    if x == -1:
                        PAchar = PAchar + word[i]
                        index += 1
                    else:
                        break
                NAchar = ''.join(wordlist[(index):])                       
        except:
            PAchar = PAchar + word[0]
            index += 1
            NAchar = word[(index):]
            print('fak')  
    else:
        PAchar = word
        NAchar = ''         
    print(PAchar, NAchar)
    if NAchar != '' and PAchar == '':         
            randindex = random.choice([2,4,5])
            NA_x,NA_y = nguyen_am_ids.get(NAchar, (-1,-1))
            #print(dau_cau, randindex)
            if dau_cau == 0:
                    dau_cau += 1
            PAnum = M82numPA[randindex][dau_cau-1] + M82dau[dau_cau-1][M82charPA[randindex].index(' ')]
            NAnum = M82numNA[NA_x][dau_cau-1] + M82dau[dau_cau-1][NA_y]
    elif NAchar == '' and PAchar != '':
        #PAchar = PAchar.capitalize()
        x, y = phu_am_ids.get(PAchar, (-1, -1))
        #print(x, y)
        if x != -1:
            if dau_cau == 0:
                    dau_cau += 1
            randindex = random.choice([0,4,5,8,9,12,14])
            PAnum = M82numPA[x][dau_cau-1] + M82dau[dau_cau-1][y]
            if randindex == 4 or randindex == 5:
                if random.choice([1,2]) == 1:
                    NAnum = M82numNA[randindex][dau_cau-1] + M82dau[dau_cau-1][M82charNA[randindex].index('  ')]
                else: NAnum = M82numNA[randindex][dau_cau-1] + M82dau[dau_cau-1][M82charNA[randindex].index(' ')]
            else: NAnum = M82numNA[randindex][dau_cau-1] + M82dau[dau_cau-1][M82charNA[randindex].index(' ')]
        else:
            x, y = nguyen_am_ids.get(word, (-1, -1))
            if dau_cau == 0:
                dau_cau += 1
            randindex = random.choice([2,4,5])
            PAnum = M82numPA[randindex][dau_cau-1] + M82dau[dau_cau-1][M82charPA[randindex].index(' ')]
            NAnum = M82numNA[x][dau_cau-1] + M82dau[dau_cau-1][y]  
    else:
        #PAchar = PAchar.capitalize()
        NA_x,NA_y = nguyen_am_ids.get(NAchar, (-1,-1))
        PA_x,PA_y = phu_am_ids.get(PAchar, (-1,-1))
        if dau_cau == 0:
                dau_cau += 1
        PAnum = M82numPA[PA_x][dau_cau-1] + M82dau[dau_cau-1][PA_y]
        NAnum = M82numNA[NA_x][dau_cau-1] + M82dau[dau_cau-1][NA_y]       
    return (PAnum + NAnum)
def Encodesent(sent):
    sent = sent.lower()
    newsent = convert_unicode(sent)
    words = newsent.split()
    num82 = []
    contcheck = 0
    randindex = random.choice([0,1])
    for index in range(len(words)):
        if contcheck > 0:
            contcheck = contcheck - 1
            continue
        else:
            word = chuan_hoa_dau_tu_tieng_viet(words[index])
            try:
                if word in specPA and randindex == 1:
                    if specPA[word] == 1:
                        num82.append(EncodeW(word, 1))         
                    elif specPA[word] == words[index + 1]:        
                        if specPA[word] == 'lục' and words[index + 2] in PLnum:
                            newword = word + ' '+ ''.join(words[index+1]) + ' ' + ''.join(words[index+2])
                            num82.append(EncodeW(newword, 1))
                            contcheck = 2  
                        elif specPA[word] == 'lục' and not(words[index + 2] in PLnum): 
                            words[index] = EncodeW(word, 0)
                        else:
                            newword = word + ' '+ ''.join(words[index+1])
                            num82.append(EncodeW(newword, 1))
                            contcheck = 1
                    else:     
                        num82.append(EncodeW(word, 0))
                else:     
                    num82.append(EncodeW(word, 0))
            except:
                print(sys.exc_info())
                num82.append(EncodeW(newword, 0))
        #print(num82)
    return ' '.join(num82)


if __name__ == '__main__':
    xxx = [['69309' ,'98288' ,'28415' ,'58588' ,'30280'],
['68841' ,'17263' ,'47662' ,'25203' ,'16695'],
['98246' ,'24972' ,'59837' ,'48136' ,'38445'],
['26837' ,'94273' ,'03798' ,'03432' ,'23248'],
['34248' ,'44248' ,'49280' ,'49260' ,'47116'],
['69598' ,'14865' ,'51684' ,'48293' ,'74331'],
['81734' ,'69579' ,'03415' ,'17897' ,'10684'],
['47861' ,'49401' ,'15285' ,'58588' ,'69588']
]
    aaa = ['xczxc','ấccas']
    setX = set(aaa)

    aaa = ['90239', '69119', '74395', '84578', '79023', '81569', '08239', '46263', '03459', '14435', '30258']
    #for i in (range(len(aaa))):
        #print(DecodeN(aaa[i]))
    
   # print(DecodeNs('9á4272'))
