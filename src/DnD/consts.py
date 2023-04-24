
FILTERID_TO_CLASS = {
    12: "Бард", 13: "Жрец", 16: "Паладин", 17: "Следопыт",
    19: "Чародей", 20: "Колдун", 21: "Волшебник", 22: "Друид",
    23: "Изобретатель",
}

FILTERID_TO_TYPE = {
    1: "Чудесный предмет", 2: "Зелье", 3: "Кольцо", 4: "Свиток",
    5: "Волшебная палочка", 6: "Жезл", 7: "Посох", 8: "Доспех",
    9: "Оружие", 19: "Гуманоид", 20: "Нежить", 21: "Дракон",
    22: "Зверь", 23: "Монстр", 24: "Аберрация", 25: "Великан",
    26: "Растение", 27: "Слизь", 28: "Небожитель", 29: "Конструкт",
    30: "Элементаль", 31: "Исчадие", 32: "Фея", 33: "Транспорт", 34: "Объект",
}

FILTERID_TO_SIZE = {
    1: "Крошечный", 2: "Маленький", 3: "Средний", 4: "Большой",
    5: "Огромный", 6: "Громадный", 7: "Средний рой крошечных",
    8: "Большой рой крошечных", 9: "Большой рой средних",
    10: "Маленький или средний", 11: "Маленький рой крошечных",
}

FILTERID_TO_LANGUAGE = {
    12: "Общий", 13: "Гномий", 14: "Дварфский", 15: "Полуросликов",
    16: "Эльфийский", 17: "Орочий", 18: "Великаний", 19: "Гоблинский",
    20: "Драконий", 21: "Бездны", 22: "Глубинная речь", 23: "Инфернальный",
    24: "Небесный", 25: "Первичный", 26: "Подземный", 27: "Сильван",
    28: "Ауран", 29: "Телепатия", 30: "Все", 31: "Гитский",
    32: "Язык Жаболюдов", 33: "Акван", 34: "Терран", 35: "Игнан",
    36: "Гноллий", 37: "Язык Греллов", 38: "Язык Крюкастых ужасов",
    39: "Модронский", 40: "Отиджский", 41: "Сахуагинский", 42: "Слаадский",
    43: "Язык Сфинксов", 44: "Три-кринский", 45: "Друидический",
    46: "Троглодитский", 47: "Язык Бурых увальней", 48: "Язык Йети",
    49: "Язык Воргов", 50: "Язык Гигантских сов", 51: "Язык Гигантских лосей",
    52: "Язык Гигантских орлов", 53: "Язык Мерцающих псов",
    54: "Язык Полярных волков", 55: "Воровской жаргон",
    56: "Язык Ледяных жаб", 57: "Тэйский", 58: "Язык Вегепигмеев",
    59: "Язык Грунгов", 60: "Язык Тлинкалли", 61: "Бохти", 62: "Мерфолк",
    63: "Крутик", 64: "Куори", 65: "Йикариа", 66: "Язык Икситксачитлов",
    67: "Леонинский", 68: "Язык Глубинных воронов", 69: "Зиксвет",
    70: "Тлетлахтолли", 71: "Язык Аартуков", 72: "Доварский",
    73: "Язык Хадози", 74: "Крауль", 75: "Любой", 76: "Умбрал",
    77: "Язык Минотавров", 78: "Язык Локсодонов", 79: "Ведалкен",
    80: "Соламнийский", 81: "Наречие кендеров", 99999: "",
}

FILTERID_TO_ENVIRONMENT = {
    1: "Арктика", 2: "Болото", 3: "Город", 4: "Горы",
    5: "Лес", 6: "Луг", 7: "Побережье", 8: "Под водой",
    9: "Подземье", 10: "Пустыня", 11: "Холмы",
}

FILTERID_TO_QUALITY = {
    1: "Необычный", 2: "Редкий", 3: "Очень редкий",
    4: "Легендарный", 5: "Редкость варьируется",
    6: "Обычный", 7: "Артефакт", 8: "Не имеет редкости",
}

FILTERID_TO_SET = {
    1: "Не требуется настройка", 2: "Требуется настройка",
}

FILTERID_TO_ARCHETYPE = {
    107: {"class": "Бард", "archetype": "Коллегия духов"},
    135: {"class": "Волшебник", "archetype": "Магия хронургии"},
    136: {"class": "Волшебник", "archetype": "Магия гравитургии"},
    139: {"class": "Друид", "archetype": "Круг земли"},
    143: {"class": "Друид", "archetype": "Круг дикого огня"},
    144: {"class": "Друид", "archetype": "Круг звёзд"},
    145: {"class": "Друид", "archetype": "Круг спор"},
    146: {"class": "Жрец", "archetype": "Домен бури"},
    147: {"class": "Жрец", "archetype": "Домен войны"},
    148: {"class": "Жрец", "archetype": "Домен жизни"},
    149: {"class": "Жрец", "archetype": "Домен знаний"},
    150: {"class": "Жрец", "archetype": "Домен обмана"},
    151: {"class": "Жрец", "archetype": "Домен природы"},
    152: {"class": "Жрец", "archetype": "Домен света"},
    153: {"class": "Жрец", "archetype": "Домен смерти"},
    154: {"class": "Жрец", "archetype": "Домен магии"},
    155: {"class": "Жрец", "archetype": "Домен кузни"},
    156: {"class": "Жрец", "archetype": "Домен упокоения"},
    157: {"class": "Жрец", "archetype": "Домен мира"},
    158: {"class": "Жрец", "archetype": "Домен порядка"},
    159: {"class": "Жрец", "archetype": "Домен сумерек"},
    160: {"class": "Изобретатель", "archetype": "Алхимик"},
    161: {"class": "Изобретатель", "archetype": "Артиллерист"},
    162: {"class": "Изобретатель", "archetype": "Боевой кузнец"},
    163: {"class": "Изобретатель", "archetype": "Бронник"},
    164: {"class": "Колдун", "archetype": "Архифея"},
    165: {"class": "Колдун", "archetype": "Исчадие"},
    166: {"class": "Колдун", "archetype": "Великий Древний"},
    167: {"class": "Колдун", "archetype": "Бессмертный"},
    168: {"class": "Колдун", "archetype": "Ведьмовской клинок"},
    169: {"class": "Колдун", "archetype": "Небожитель"},
    170: {"class": "Колдун", "archetype": "Бездонный"},
    171: {"class": "Колдун", "archetype": "Гений"},
    172: {"class": "Колдун", "archetype": "Нежить"},
    174: {"class": "Монах", "archetype": "Путь тени"},
    175: {"class": "Монах", "archetype": "Путь четырёх стихий"},
    179: {"class": "Монах", "archetype": "Путь солнечной души"},
    183: {"class": "Паладин", "archetype": "Клятва преданности"},
    184: {"class": "Паладин", "archetype": "Клятва древних"},
    185: {"class": "Паладин", "archetype": "Клятва мести"},
    186: {"class": "Паладин", "archetype": "Клятвопреступник"},
    187: {"class": "Паладин", "archetype": "Клятва короны"},
    188: {"class": "Паладин", "archetype": "Клятва искупления"},
    189: {"class": "Паладин", "archetype": "Клятва покорения"},
    190: {"class": "Паладин", "archetype": "Клятва славы"},
    191: {"class": "Паладин", "archetype": "Клятва смотрителей"},
    194: {"class": "Плут", "archetype": "Мистический ловкач"},
    203: {"class": "Следопыт", "archetype": "Странник горизонта"},
    204: {"class": "Следопыт", "archetype": "Сумрачный охотник"},
    205: {"class": "Следопыт", "archetype": "Убийца монстров"},
    206: {"class": "Следопыт", "archetype": "Странник фей"},
    207: {"class": "Следопыт", "archetype": "Хранитель роя"},
    208: {"class": "Следопыт", "archetype": "Наездник на дрейке"},
    211: {"class": "Чародей", "archetype": "Божественная душа"},
    212: {"class": "Чародей", "archetype": "Теневая магия"},
    214: {"class": "Чародей", "archetype": "Аберрантный разум"},
    215: {"class": "Чародей", "archetype": "Заводная душа"},
    286: {"class": "Чародей", "archetype": "Лунное чародейство"},
}

FILTERID_TO_SOURCE = {
    101: "Dungeon master's guide",
    102: "Player's handbook",
    103: "Monster manual",
    105: "Hoard of the Dragon Queen",
    106: "The Rise of Tiamat",
    107: "Princes of the Apocalypse",
    108: "Sword Coast Adventurer's Guide",
    109: "Xanathar's Guide to Everything",
    110: "Lost Mine of Phandelver",
    111: "Volo's guide to monsters",
    112: "Guildmasters' guide to Ravnica",
    113: "Mordenkainen's Tome of Foes",
    114: "Tomb of Annihilation",
    115: "Acquisition Incorporated",
    116: "Explorer's Guide to Wildemount",
    117: "Tasha's Cauldron of Everything",
    119: "Eberron: Rising from the Last War",
    120: "Icewind Dale: Rime of the Frostmaiden",
    121: "Mythic Odysseys of Theros",
    122: "Candlekeep Mysteries",
    123: "Hunt for the Thessalhydra",
    124: "Curse of Strahd",
    125: "Van Richten's Guide to Ravenloft",
    126: "Baldur's Gate: Descent Into Avernus",
    127: "Essentials Kit: Divine Contention",
    128: "Ghosts of Saltmarsh",
    129: "Out of the Abyss",
    130: "The Lost Dungeon of Rickedness: Big Rick Energy",
    131: "Essentials Kit: Sleeping Dragon's Wake",
    132: "Storm King's Thunder",
    133: "Tales from the Yawning Portal",
    134: "Waterdeep: Dragon Heist",
    135: "Waterdeep: Dungeon of the Mad Mage",
    151: "The Wild Beyond The Witchlight: A Feywild Adventure",
    152: "Fizban's Treasury of Dragons",
    153: "Lost Laboratory of Kwalish",
    155: "Strixhaven: A Curriculum of Chaos",
    157: "Essentials Kit: Dragon of Icespire peak",
    158: "Mordenkainen Presents: Monsters of the Multiverse",
    159: "Critical Role: Call of the Netherdeep",
    160: "Spelljammer: Adventures in Space",
    161: "Infernal Machine Rebuild",
    167: "Essentials Kit: Storm Lord's Wrath",
    169: "Adventurers League",
    171: "Journeys through the Radiant Citadel",
    174: "The Vecna Dossier",
    180: "Saltmarsh Encounters",
    183: "Dragonlance: Shadow of the Dragon Queen",
    187: "Monstrous Compendium Vol 1: Spelljammer Creatures",
    188: "Monstrous Compendium Vol 2: Dragonlance Creatures",
    189: "Keys from the Golden Vault",
    191: "Honor among Thieves",

}


FILTER_TO_ALINGMENT = {
    "lg": "Законно-добрый", "ng": "Нейтрально-добрый",
    "cg": "Хаотично-добрый", "ln": "Законно-нейтральный",
    "n": "Нейтральный", "cn": "Хаотично-нейтральный",
    "le": "Законно-злой", "ne": "Нейтрально-злой",
    "ce": "Хаотично-злой", "none": "",

}

FILTER_TO_ABILITY = {
    "ability.STR": "Сила",
    "ability.DEX": "Ловкость",
    "ability.CON": "Телосложение",
    "ability.INT": "Интеллект",
    "ability.WIS": "Мудрость",
    "ability.CHA": "Харизма",
}

FILTER_TO_SKILL = {
    "skill.acrobatics": "Акробатика",
    "skill.athletics": "Атлетика",
    "skill.perception": "Восприятие",
    "skill.performance": "Выступление",
    "skill.deception": "Обман",
    "skill.investigation": "Расследование",
}

FILTER_TO_PROFIENCY = {
    "proficiency.skill": "навык",
    "proficiency.tools": "инструмент",
    "proficiency.weapon": "оружие",
    "proficiency.armor": "броня",
    "proficiency.language": "язык",
}

FILTER_TO_REQUIRE = {
    "requires.spellcasting": "заклинатель",
    "requires.race": "раса",
    "requires.class": "класс",
    "requires.ability.STR": "Сила",
    "requires.ability.DEX": "Ловкость",
    "requires.ability.CON": "Телосложение",
    "requires.ability.INT": "Интеллект",
    "requires.ability.WIS": "Мудрость",
    "requires.ability.CHA": "Харизма",
}

FILTER_TO_OTHER = {
    "weapon": "оружейная",
    "armor": "доспешная",
    "magic": "магическая",
    "AC": "влияет на КД",
    "spellsource": "даёт заклинание",
}


SPELL_HTML_CONST = '''
<a href="" itemprop="url" class="item-link">NONE</a>

<ul class="params">
    <li class="size-type-alignment">NONE</li>
    <li><strong>Время накладывания: </strong>NONE</li>
    <li><strong>Дистанция:</strong> NONE</li>
    <li><strong>Компоненты:</strong> NONE</li>
    <li><strong>Длительность:</strong> NONE</li>
    <li><strong>Классы:</strong> NONE</li>
    <li><strong>Архетипы:</strong> NONE</li>
    <li><strong>Источник:</strong> NONE</li>
    <li class="subsection desc">
        <div itemprop="description">
            <p>NONE</p>
        </div>
    </li>
</ul>'''

ITEM_HTML_CONST = '''
<a href="" itemprop="url" class="item-link">NONE</a>

<ul class="params">
    <li class="size-type-alignment">NONE</li>
    <li><strong>Источник:</strong> NONE</li>
    <li class="subsection desc">
        <div itemprop="description">
            <p>NONE</p>
        </div>
    </li>
</ul>'''

BESTIARY_HTML_CONST = '''
<a href="" itemprop="url" class="item-link">NONE</a>

<ul class="params">
    <li class="size-type-alignment">NONE</li>
    <li><strong>Источник:</strong> NONE</li>
    <li class="subsection desc">
        <div itemprop="description">
            <p>NONE</p>
        </div>
    </li>
</ul>'''

FEATS_HTML_CONST = '''
<a href="" itemprop="url" class="item-link">NONE</a>

<ul class="params">
    <li class="size-type-alignment">NONE</li>
    <li><strong>Источник:</strong> NONE</li>
    <li class="subsection desc">
        <div itemprop="description">
            <p>NONE</p>
        </div>
    </li>
</ul>'''
