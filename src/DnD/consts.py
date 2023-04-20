FILTERID_TO_CLASS = {
    12: "Бард", 13: "Жрец", 16: "Паладин", 17: "Следопыт",
    19: "Чародей", 20: "Колдун", 21: "Волшебник", 22: "Друид",
    23: "Изобретатель"}
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
    102: "Player's handbook",
    107: "Princes of the Apocalypse",
    108: "Sword Coast Adventurer's Guide",
    109: "Xanathar's Guide to Everything",
    112: "Guildmasters' guide to Ravnica",
    115: "Acquisition Incorporated",
    116: "Explorer's Guide to Wildemount",
    117: "Tasha's Cauldron of Everything",
    120: "Icewind Dale: Rime of the Frostmaiden",
    152: "Fizban's Treasury of Dragons",
    153: "Lost Laboratory of Kwalish",
    155: "Strixhaven: A Curriculum of Chaos",
    160: "Spelljammer: Adventures in Space",

}


SPELL_HTML_CONST = '''
<a href="/spells/4-aura_of_life/" itemprop="url" class="item-link">NONE</a>

<ul class="params">
    <li class="size-type-alignment">NONE</li>
    <li><strong>Время накладывания:</strong>NONE</li>
    <li><strong>Дистанция:</strong>NONE</li>
    <li><strong>Компоненты:</strong>NONE</li>
    <li><strong>Длительность:</strong>NONE</li>
    <li><strong>Классы:</strong>NONE</li>
    <li><strong>Архетипы:</strong>NONE</li>
    <li><strong>Источник:</strong> NONE</li>
    <li class="subsection desc">
        <div itemprop="description">
            <p>NONE</p>
        </div>
    </li>
</ul>'''
