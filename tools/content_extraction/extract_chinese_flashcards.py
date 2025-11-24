#!/usr/bin/env python3
"""
TCM Chinese Character Flashcard Generator

This script extracts Chinese characters (hanzi) and pinyin from TCM knowledge base files
(points, herbs, formulas, symptoms, patterns) and generates comprehensive flashcards with:
- Full term in hanzi and pinyin
- Individual character breakdown with meanings and pronunciation
- Stroke order animations (strokeorder.com style)
- Character etymology and radicals
- Makemeahanzi stroke order data

Dependencies:
    pip install pyyaml pypinyin hanziconv requests beautifulsoup4

Optional for enhanced features:
    pip install hanzi-writer-data
"""

import json
import re
import unicodedata
import urllib.parse
from collections import defaultdict
from pathlib import Path

import yaml


class ChineseCharacterExtractor:
    """Extract Chinese characters and pinyin from TCM knowledge base files."""

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.chinese_terms: dict[str, dict] = {}
        self.all_characters: set[str] = set()

        # Directories to scan
        self.scan_dirs = ["TCM_Points", "TCM_Herbs", "TCM_Formulas", "TCM_Symptoms", "TCM_Patterns"]

    def is_chinese_char(self, char: str) -> bool:
        """Check if a character is Chinese (CJK Unified Ideographs)."""
        try:
            return "\u4e00" <= char <= "\u9fff"
        except:
            return False

    def extract_chinese_text(self, text: str) -> list[str]:
        """Extract sequences of Chinese characters from text."""
        if not text:
            return []

        chinese_sequences = []
        current_sequence = []

        for char in text:
            if self.is_chinese_char(char):
                current_sequence.append(char)
            else:
                if current_sequence:
                    chinese_sequences.append("".join(current_sequence))
                    current_sequence = []

        if current_sequence:
            chinese_sequences.append("".join(current_sequence))

        return chinese_sequences

    def parse_frontmatter(self, file_path: Path) -> dict | None:
        """Parse YAML frontmatter from markdown file."""
        try:
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

            # Extract frontmatter between --- markers
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
            if match:
                frontmatter_text = match.group(1)
                return yaml.safe_load(frontmatter_text)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

        return None

    def extract_from_file(self, file_path: Path, file_type: str) -> None:
        """Extract Chinese terms from a single file."""
        frontmatter = self.parse_frontmatter(file_path)
        if not frontmatter:
            return

        # Extract based on file type
        if file_type == "point" and "point_data" in frontmatter:
            self._extract_point_data(frontmatter["point_data"], file_path)

        elif file_type == "herb" and "herb_data" in frontmatter:
            self._extract_herb_data(frontmatter["herb_data"], file_path)

        elif file_type == "formula":
            self._extract_formula_data(frontmatter, file_path)

        elif file_type == "pattern":
            self._extract_pattern_data(frontmatter, file_path)

        elif file_type == "symptom":
            self._extract_symptom_data(frontmatter, file_path)

    def _extract_point_data(self, point_data: dict, file_path: Path) -> None:
        """Extract Chinese from acupuncture point data."""
        hanzi = point_data.get("hanzi", "")
        pinyin = point_data.get("pinyin", "")
        english = point_data.get("english", "")
        code = point_data.get("code", "")

        if hanzi:
            self._add_term(hanzi, pinyin, english, "acupuncture_point", str(file_path), code)

    def _extract_herb_data(self, herb_data: dict, file_path: Path) -> None:
        """Extract Chinese from herb data."""
        hanzi = herb_data.get("hanzi", "")
        pinyin = herb_data.get("pinyin", "")
        english = herb_data.get("english", "")
        pharmaceutical = herb_data.get("pharmaceutical", "")

        if hanzi:
            self._add_term(hanzi, pinyin, english, "herb", str(file_path), pharmaceutical)

    def _extract_formula_data(self, frontmatter: dict, file_path: Path) -> None:
        """Extract Chinese from formula data."""
        name = frontmatter.get("name", "")

        # Extract Chinese from formula name
        chinese_sequences = self.extract_chinese_text(name)

        # Try to extract from file name if not in frontmatter
        if not chinese_sequences:
            file_name = file_path.stem
            chinese_sequences = self.extract_chinese_text(file_name)

        for hanzi in chinese_sequences:
            if len(hanzi) >= 2:  # Only meaningful terms
                self._add_term(hanzi, "", name, "formula", str(file_path), "")

    def _extract_pattern_data(self, frontmatter: dict, file_path: Path) -> None:
        """Extract Chinese from pattern data."""
        name = frontmatter.get("name", "")
        chinese_sequences = self.extract_chinese_text(name)

        for hanzi in chinese_sequences:
            if len(hanzi) >= 2:
                self._add_term(hanzi, "", name, "pattern", str(file_path), "")

    def _extract_symptom_data(self, frontmatter: dict, file_path: Path) -> None:
        """Extract Chinese from symptom data."""
        name = frontmatter.get("name", "")
        chinese_sequences = self.extract_chinese_text(name)

        for hanzi in chinese_sequences:
            if len(hanzi) >= 2:
                self._add_term(hanzi, "", name, "symptom", str(file_path), "")

    def _add_term(
        self, hanzi: str, pinyin: str, english: str, category: str, source_file: str, additional_info: str
    ) -> None:
        """Add a Chinese term to the collection."""
        if not hanzi:
            return

        # Add individual characters to set
        for char in hanzi:
            if self.is_chinese_char(char):
                self.all_characters.add(char)

        # Store term information
        if hanzi not in self.chinese_terms:
            self.chinese_terms[hanzi] = {
                "hanzi": hanzi,
                "pinyin": pinyin,
                "english": english,
                "category": category,
                "sources": [source_file],
                "additional_info": additional_info,
                "character_count": len(hanzi),
            }
        else:
            # Add source if not already present
            if source_file not in self.chinese_terms[hanzi]["sources"]:
                self.chinese_terms[hanzi]["sources"].append(source_file)

    def scan_all_files(self) -> None:
        """Scan all TCM knowledge base files."""
        print("Scanning TCM knowledge base files...")

        for dir_name in self.scan_dirs:
            dir_path = self.base_path / dir_name

            if not dir_path.exists():
                print(f"Directory not found: {dir_path}")
                continue

            print(f"\nScanning {dir_name}...")

            # Determine file type from directory name
            file_type = dir_name.lower().replace("tcm_", "").rstrip("s")

            # Recursively scan all .md files
            md_files = list(dir_path.rglob("*.md"))

            for file_path in md_files:
                # Skip backup files
                if ".backup" in str(file_path):
                    continue

                self.extract_from_file(file_path, file_type)

            print(f"  Found {len(md_files)} files")

        print("\n✓ Extraction complete!")
        print(f"  Total unique terms: {len(self.chinese_terms)}")
        print(f"  Total unique characters: {len(self.all_characters)}")

    def get_statistics(self) -> dict:
        """Get statistics about extracted data."""
        stats = {
            "total_terms": len(self.chinese_terms),
            "total_characters": len(self.all_characters),
            "by_category": defaultdict(int),
            "by_character_count": defaultdict(int),
        }

        for term_data in self.chinese_terms.values():
            stats["by_category"][term_data["category"]] += 1
            stats["by_character_count"][term_data["character_count"]] += 1

        return stats


class StrokeOrderProvider:
    """Provide stroke order information and animations."""

    def __init__(self, cache_dir: str = None):
        self.cache_dir = Path(cache_dir) if cache_dir else Path("stroke_order_cache")
        self.cache_dir.mkdir(exist_ok=True)

        # Try to load makemeahanzi data if available
        self.hanzi_writer_data = {}
        self._load_hanzi_writer_data()

    def _load_hanzi_writer_data(self) -> None:
        """Load hanzi-writer-data if available."""
        try:
            # This would load from hanzi-writer-data package if installed
            # For now, we'll use online resources
            pass
        except:
            pass

    def get_strokeorder_url(self, char: str) -> str:
        """Get strokeorder.com URL for a character."""
        return f"https://strokeorder.com/mandarin/{urllib.parse.quote(char)}"

    def get_animated_gif_url(self, char: str) -> str:
        """Get animated GIF URL for stroke order (if available)."""
        # strokeorder.com uses this pattern for their animations
        unicode_hex = f"{ord(char):04x}"
        return f"https://strokeorder.com/assets/anims/{unicode_hex}.gif"

    def get_hanzi_writer_svg(self, char: str) -> str | None:
        """Get SVG path data for HanziWriter animations."""
        # HanziWriter uses JSON data files
        unicode_hex = f"{ord(char):05x}"
        return f"https://cdn.jsdelivr.net/npm/hanzi-writer-data@latest/{unicode_hex}.json"

    def get_stroke_order_html(self, char: str) -> str:
        """Generate HTML with embedded stroke order animation."""
        unicode_hex = f"{ord(char):04x}"

        html = f"""
<div class="stroke-order-container" data-char="{char}">
    <h3>{char}</h3>
    
    <!-- StrokeOrder.com style animation -->
    <div class="stroke-animation">
        <img src="https://strokeorder.com/assets/anims/{unicode_hex}.gif" 
             alt="Stroke order for {char}"
             onerror="this.style.display='none'">
    </div>
    
    <!-- HanziWriter interactive animation -->
    <div id="hanzi-writer-{unicode_hex}" class="hanzi-writer"></div>
    
    <script src="https://cdn.jsdelivr.net/npm/hanzi-writer@3"></script>
    <script>
        var writer = HanziWriter.create('hanzi-writer-{unicode_hex}', '{char}', {{
            width: 200,
            height: 200,
            padding: 5,
            showOutline: true,
            strokeAnimationSpeed: 1,
            delayBetweenStrokes: 200
        }});
        writer.loopCharacterAnimation();
    </script>
    
    <!-- Link to strokeorder.com for full details -->
    <p><a href="https://strokeorder.com/mandarin/{urllib.parse.quote(char)}" 
          target="_blank">View on StrokeOrder.com</a></p>
</div>
"""
        return html

    def get_stroke_order_info(self, char: str) -> dict:
        """Get comprehensive stroke order information."""
        return {
            "character": char,
            "unicode": f"U+{ord(char):04X}",
            "strokeorder_url": self.get_strokeorder_url(char),
            "animated_gif_url": self.get_animated_gif_url(char),
            "hanzi_writer_json": self.get_hanzi_writer_svg(char),
            "html_animation": self.get_stroke_order_html(char),
        }


class ChineseCharacterAnalyzer:
    """Analyze Chinese characters and generate detailed information."""

    def __init__(self, stroke_order_provider: StrokeOrderProvider = None):
        self.character_data: dict[str, dict] = {}
        self.stroke_order = stroke_order_provider or StrokeOrderProvider()

        # Try to import optional libraries
        try:
            from pypinyin import Style, pinyin

            self.pypinyin = pinyin
            self.pinyin_style = Style
            self.has_pypinyin = True
        except ImportError:
            print("Warning: pypinyin not installed. Pinyin generation will be limited.")
            self.has_pypinyin = False

        # Try to import radical library
        try:
            from cjkradlib.decompose import Decompose

            self.decomposer = Decompose()
            self.has_cjkradlib = True
        except ImportError:
            print("Warning: cjkradlib not installed. Radical information will be limited.")
            self.has_cjkradlib = False
            self.decomposer = None

        # Load basic character meanings dictionary
        self.basic_meanings = self._load_basic_meanings()
        print(f"Loaded {len(self.basic_meanings)} basic character meanings")

        # Load radical meanings dictionary
        self.radical_meanings = self._load_radical_meanings()
        print(f"Loaded {len(self.radical_meanings)} radical meanings")

    def _load_basic_meanings(self) -> dict[str, str]:
        """Load basic character meanings from a simple dictionary."""
        # Basic TCM-relevant character meanings
        # This is a starter set - can be expanded
        return {
            "中": "middle, center",
            "医": "medicine, doctor",
            "学": "study, learn",
            "气": "qi, energy, air",
            "血": "blood",
            "阴": "yin, shade",
            "阳": "yang, sun",
            "脾": "spleen",
            "胃": "stomach",
            "肝": "liver",
            "心": "heart",
            "肺": "lung",
            "肾": "kidney",
            "经": "channel, meridian",
            "络": "collateral, network",
            "穴": "point, cavity",
            "针": "needle",
            "灸": "moxibustion",
            "虚": "deficiency, empty",
            "实": "excess, full",
            "寒": "cold",
            "热": "heat",
            "湿": "damp",
            "燥": "dry",
            "风": "wind",
            "火": "fire",
            "水": "water",
            "木": "wood",
            "金": "metal",
            "土": "earth",
            "上": "up, above",
            "下": "down, below",
            "内": "inside, internal",
            "外": "outside, external",
            "左": "left",
            "右": "right",
            "前": "front",
            "后": "back, behind",
            "大": "big, great",
            "小": "small, little",
            "长": "long",
            "短": "short",
            "高": "high, tall",
            "低": "low",
            "新": "new",
            "旧": "old",
            "痛": "pain",
            "痒": "itch",
            "麻": "numb",
            "胀": "distension",
            "满": "fullness",
            "泻": "diarrhea, drain",
            "补": "tonify, supplement",
            "清": "clear",
            "温": "warm",
            "凉": "cool",
            "平": "neutral, level",
            "升": "ascend, raise",
            "降": "descend, lower",
            "散": "disperse",
            "收": "gather, astringent",
            "开": "open",
            "合": "close, unite",
            "通": "pass through",
            "滞": "stagnate",
            "行": "move, travel",
            "止": "stop",
            "生": "generate, birth",
            "克": "control, restrain",
            "化": "transform",
            "精": "essence, refined",
            "神": "spirit, mind",
            "魂": "ethereal soul",
            "魄": "corporeal soul",
            "志": "will, intention",
            "意": "thought, idea",
            "智": "wisdom",
            "力": "strength, power",
            "能": "ability, can",
            "功": "function, merit",
            "效": "effect, efficacy",
            "病": "disease, illness",
            "症": "symptom",
            "证": "pattern, syndrome",
            "治": "treat, cure",
            "方": "formula, prescription",
            "药": "medicine, herb",
            "草": "grass, herb",
            "根": "root",
            "茎": "stem",
            "叶": "leaf",
            "花": "flower",
            "果": "fruit",
            "子": "seed, child",
            "皮": "skin, peel",
            "肉": "flesh, meat",
            "骨": "bone",
            "筋": "sinew, tendon",
            "脉": "vessel, pulse",
            "汗": "sweat",
            "尿": "urine",
            "便": "stool, convenient",
            "津": "fluid",
            "液": "liquid, fluid",
            "痰": "phlegm",
            "涎": "saliva",
            "涕": "nasal mucus",
            "泪": "tears",
            "三": "three",
            "四": "four",
            "五": "five",
            "六": "six",
            "七": "seven",
            "八": "eight",
            "九": "nine",
            "十": "ten",
            "百": "hundred",
            "千": "thousand",
            "万": "ten thousand",
            "一": "one",
            "二": "two",
            "人": "person, human",
            "天": "heaven, sky",
            "地": "earth, ground",
            "日": "sun, day",
            "月": "moon, month",
            "年": "year",
            "时": "time, hour",
            "春": "spring",
            "夏": "summer",
            "秋": "autumn",
            "冬": "winter",
            "东": "east",
            "西": "west",
            "南": "south",
            "北": "north",
            "手": "hand",
            "足": "foot",
            "头": "head",
            "面": "face",
            "目": "eye",
            "耳": "ear",
            "鼻": "nose",
            "口": "mouth",
            "舌": "tongue",
            "齿": "teeth",
            "喉": "throat",
            "颈": "neck",
            "肩": "shoulder",
            "背": "back",
            "腰": "waist, lower back",
            "腹": "abdomen",
            "胸": "chest",
            "乳": "breast, milk",
            "臂": "arm",
            "肘": "elbow",
            "腕": "wrist",
            "指": "finger",
            "掌": "palm",
            "腿": "leg",
            "膝": "knee",
            "踝": "ankle",
            "趾": "toe",
            "白": "white",
            "黑": "black",
            "红": "red",
            "黄": "yellow",
            "青": "green, blue",
            "紫": "purple",
            "色": "color",
            "声": "sound, voice",
            "味": "taste, flavor",
            "香": "fragrant, aromatic",
            "臭": "odor, smell",
            "甘": "sweet",
            "苦": "bitter",
            "酸": "sour",
            "辛": "acrid, spicy",
            "咸": "salty",
            "淡": "bland",
            "涩": "astringent",
            "滑": "slippery",
            "粗": "rough, coarse",
            "细": "fine, thin",
            "软": "soft",
            "硬": "hard",
            "轻": "light",
            "重": "heavy",
            "快": "fast, quick",
            "慢": "slow",
            "强": "strong",
            "弱": "weak",
            "多": "many, much",
            "少": "few, little",
            "有": "have, exist",
            "无": "not have, without",
            "是": "be, yes",
            "非": "not, wrong",
            "正": "correct, upright",
            "邪": "evil, pathogenic",
            "真": "true, genuine",
            "假": "false, fake",
            "好": "good",
            "坏": "bad",
            "安": "peaceful, calm",
            "危": "danger",
            "吉": "auspicious",
            "凶": "inauspicious",
            "福": "blessing, fortune",
            "祸": "disaster",
            "喜": "joy, happy",
            "怒": "anger",
            "忧": "worry, anxiety",
            "思": "think, thought",
            "悲": "sadness",
            "恐": "fear",
            "惊": "fright, startle",
            # Additional TCM-relevant characters (curated list)
            "丁": "nail, robust",
            "不": "not, no",
            "丘": "hill, mound",
            "丝": "silk, thread",
            "丹": "cinnabar, red pill",
            "乌": "crow, black",
            "乙": "second, bent",
            "乾": "dry, heaven",
            "井": "well",
            "交": "intersect, exchange",
            "京": "capital",
            "仁": "benevolence, kernel",
            "仙": "immortal",
            "代": "generation, substitute",
            "仲": "middle, second",
            "伏": "hide, lie down",
            "使": "use, envoy",
            "侧": "side, lateral",
            "俞": "yes, transport point",
            "信": "trust, letter",
            "倉": "warehouse",
            "偏": "slant, partial",
            "僕": "servant",
            "元": "origin, primary",
            "光": "light, bright",
            "兌": "exchange, dui",
            "兔": "rabbit",
            "党": "party, group",
            "內": "inside, internal",
            "公": "public, duke",
            "兰": "orchid",
            "决": "decide, burst",
            "冷": "cold",
            "分": "divide, minute",
            "列": "arrange, row",
            "加": "add, increase",
            "勞": "labor, toil",
            "包": "wrap, package",
            "卻": "retreat, however",
            "厘": "unit of length",
            "厚": "thick, generous",
            "厥": "reversal, faint",
            "厭": "dislike, satiated",
            "厲": "severe, strict",
            "参": "ginseng, participate",
            "參": "ginseng, participate",
            "台": "platform, stage",
            "吳": "Wu (surname)",
            "周": "Zhou, circumference",
            "命": "life, command",
            "和": "harmony, peace",
            "哀": "grief, sorrow",
            "商": "commerce, Shang",
            "啞": "mute, hoarse",
            "囟": "fontanel",
            "垣": "wall, rampart",
            "堂": "hall, main room",
            "墟": "ruins, mound",
            "复": "return, repeat",
            "夜": "night",
            "夷": "barbarian, level",
            "契": "contract, engrave",
            "女": "woman, female",
            "委": "entrust, wither",
            "姜": "ginger",
            "威": "power, prestige",
            "完": "complete, finish",
            "宗": "ancestor, clan",
            "宫": "palace, uterus",
            "宽": "wide, lenient",
            "寸": "inch, cun",
            "尺": "foot, chi",
            "尾": "tail, end",
            "居": "dwell, reside",
            "屈": "bend, crouch",
            "山": "mountain",
            "岩": "rock, cliff",
            "峰": "peak, summit",
            "崑": "Kunlun mountains",
            "崙": "Kunlun",
            "巨": "huge, giant",
            "巢": "nest",
            "川": "river, stream",
            "州": "province, state",
            "巷": "alley, lane",
            "帝": "emperor, god",
            "带": "belt, zone",
            "常": "constant, often",
            "幕": "curtain, screen",
            "干": "dry, stem",
            "幽": "secluded, dark",
            "府": "prefecture, palace",
            "度": "degree, measure",
            "座": "seat, base",
            "廉": "honest, edge",
            "廊": "corridor, porch",
            "延": "extend, prolong",
            "建": "build, establish",
            "弦": "string, bowstring",
            "张": "stretch, open",
            "归": "return, belong",
            "当": "ought, bear",
            "彩": "color, variegated",
            "影": "shadow, image",
            "役": "service, campaign",
            "往": "go, past",
            "征": "journey, levy",
            "径": "path, diameter",
            "得": "get, obtain",
            "復": "return, restore",
            "微": "tiny, subtle",
            "德": "virtue, morality",
            "忘": "forget",
            "忠": "loyalty, faithful",
            "忡": "sorrowful",
            "急": "urgent, hasty",
            "性": "nature, character",
            "息": "breath, rest",
            "悬": "hang, suspend",
            "情": "emotion, feeling",
            "惡": "evil, bad",
            "愈": "heal, recover",
            "感": "feel, sense",
            "憂": "worry, sad",
            "成": "become, succeed",
            "戶": "door, household",
            "房": "room, house",
            "扁": "flat, tablet",
            "承": "bear, inherit",
            "抑": "repress, restrain",
            "拘": "restrict, arrest",
            "持": "hold, maintain",
            "挟": "clasp, coerce",
            "振": "shake, rouse",
            "捷": "quick, victory",
            "接": "connect, receive",
            "推": "push, infer",
            "提": "lift, raise",
            "握": "grasp, hold",
            "摇": "shake, wave",
            "攒": "gather, accumulate",
            "支": "branch, support",
            "改": "change, reform",
            "攻": "attack, study",
            "放": "release, let go",
            "故": "reason, old",
            "敗": "defeat, ruin",
            "敦": "honest, sincere",
            "敬": "respect, honor",
            "斗": "fight, dipper",
            "斜": "slanting, oblique",
            "斷": "break, decide",
            "旁": "side, beside",
            "旋": "revolve, return",
            "族": "clan, race",
            "旺": "prosperous, vigorous",
            "昆": "elder brother, insect",
            "明": "bright, clear",
            "易": "easy, change",
            "映": "reflect, shine",
            "昭": "bright, manifest",
            "晴": "clear weather",
            "暑": "heat, summer",
            "暖": "warm",
            "暗": "dark, secret",
            "曲": "bent, song",
            "曹": "Cao (surname)",
            "會": "meet, can",
            "朝": "morning, dynasty",
            "期": "period, expect",
            "未": "not yet",
            "本": "root, origin",
            "朱": "vermillion, Zhu",
            "朴": "simple, plain",
            "机": "machine, opportunity",
            "杏": "apricot",
            "材": "material, timber",
            "村": "village",
            "杜": "stop, Du (surname)",
            "束": "bundle, restrain",
            "杨": "willow, Yang",
            "枝": "branch, twig",
            "枢": "pivot, hub",
            "枯": "withered, dry",
            "柏": "cypress",
            "柔": "soft, gentle",
            "柱": "pillar, post",
            "查": "examine, investigate",
            "柴": "firewood, Chai",
            "栀": "gardenia",
            "栋": "ridgepole, pillar",
            "栗": "chestnut",
            "校": "school, check",
            "核": "nucleus, kernel",
            "格": "pattern, standard",
            "桂": "cassia, laurel",
            "桃": "peach",
            "桑": "mulberry",
            "桔": "tangerine",
            "梁": "beam, bridge",
            "梅": "plum, mei",
            "梓": "catalpa tree",
            "梗": "stem, stalk",
            "條": "strip, item",
            "梨": "pear",
            "棗": "jujube, date",
            "棘": "thorny, jujube",
            "棱": "edge, corner",
            "棕": "palm tree, brown",
            "椒": "pepper",
            "楊": "willow, poplar",
            "楓": "maple",
            "楚": "clear, Chu",
            "極": "extreme, pole",
            "榆": "elm",
            "榔": "betel nut",
            "槐": "locust tree",
            "樂": "joy, music",
            "樓": "building, floor",
            "標": "mark, standard",
            "樞": "pivot, axis",
            "模": "model, pattern",
            "樸": "simple, sincere",
            "樹": "tree",
            "橋": "bridge",
            "橘": "tangerine",
            "機": "machine, chance",
            "檀": "sandalwood",
            "檳": "betel nut",
            "欠": "owe, lack",
            "次": "next, order",
            "欲": "desire, wish",
            "歌": "song, sing",
            "歸": "return, belong",
            "死": "die, death",
            "殘": "remnant, cruel",
            "殺": "kill, reduce",
            "殼": "shell, husk",
            "毒": "poison, toxin",
            "比": "compare, ratio",
            "毛": "hair, fur",
            "氏": "clan, family name",
            "民": "people, citizen",
            "氣": "qi, air, energy",
            "氛": "atmosphere",
            "氷": "ice",
            "永": "eternal, long",
            "求": "seek, request",
            "汁": "juice, sap",
            "江": "river, Yangtze",
            "池": "pond, pool",
            "汤": "soup, decoction",
            "汪": "vast, Wang",
            "沉": "sink, submerge",
            "沒": "not have, sink",
            "沖": "pour, rush",
            "沙": "sand, hoarse",
            "沛": "abundant, copious",
            "沟": "ditch, groove",
            "没": "not have, sink",
            "河": "river",
            "沸": "boil",
            "油": "oil, fat",
            "沼": "pond, marsh",
            "泉": "spring, fountain",
            "泊": "anchor, tranquil",
            "法": "law, method",
            "泡": "bubble, soak",
            "波": "wave",
            "泣": "weep, sob",
            "泥": "mud, plaster",
            "注": "pour, focus",
            "泰": "peaceful, great",
            "泽": "marsh, grace",
            "洋": "ocean, foreign",
            "洗": "wash, cleanse",
            "洛": "Luo river",
            "洞": "cave, hole",
            "洪": "flood, vast",
            "活": "live, alive",
            "流": "flow, current",
            "浅": "shallow",
            "浆": "thick liquid",
            "浊": "turbid, muddy",
            "测": "measure, survey",
            "浑": "muddy, whole",
            "浓": "thick, strong",
            "浙": "Zhejiang",
            "浮": "float, superficial",
            "海": "sea, ocean",
            "浸": "soak, immerse",
            "消": "vanish, disperse",
            "涌": "gush, surge",
            "涙": "tears",
            "涛": "large waves",
            "涝": "waterlogged",
            "涟": "ripples",
            "涣": "disperse, scatter",
            "涤": "wash, cleanse",
            "润": "moist, smooth",
            "涧": "mountain stream",
            "涨": "rise, swell",
            "涪": "Fu river",
            "涮": "rinse, scald",
            "涯": "shore, limit",
            "涵": "contain, culvert",
            "淀": "shallow lake",
            "淋": "drench, filter",
            "淑": "gentle, virtuous",
            "淘": "wash, eliminate",
            "淙": "gurgling water",
            "淤": "silt, stagnant",
            "淨": "clean, pure",
            "淩": "pure, icy",
            "淪": "sink, fall",
            "淫": "excessive, lewd",
            "淬": "temper, quench",
            "淮": "Huai river",
            "深": "deep, profound",
            "淳": "honest, pure",
            "混": "mix, confused",
            "淹": "flood, submerge",
            "添": "add, increase",
            "渇": "thirsty",
            "渉": "wade, experience",
            "渊": "abyss, deep",
            "渋": "astringent",
            "渗": "seep, permeate",
            "渚": "islet, bank",
            "減": "decrease, subtract",
            "渝": "change, Chongqing",
            "渠": "ditch, channel",
            "渡": "cross, ferry",
            "渣": "dregs, residue",
            "渥": "moisten, enrich",
            "測": "measure, test",
            "渭": "Wei river",
            "港": "harbor, port",
            "渴": "thirsty",
            "游": "swim, travel",
            "渺": "vast, minute",
            "湃": "surge",
            "湄": "bank, shore",
            "湊": "gather, happen",
            "湍": "rapid current",
            "湖": "lake",
            "湘": "Hunan, Xiang river",
            "湛": "deep, clear",
            "湧": "gush, surge",
            "湫": "marsh, damp",
            "湮": "bury, submerge",
            "湯": "hot water, soup",
            "湾": "bay, gulf",
            "満": "full, satisfied",
            "溃": "burst, fester",
            "溅": "splash",
            "溉": "irrigate",
            "源": "source, origin",
            "準": "standard, allow",
            "溜": "slip, slide",
            "溝": "ditch, groove",
            "溢": "overflow",
            "溥": "widespread",
            "溪": "stream, brook",
            "溫": "warm, mild",
            "溯": "go upstream",
            "溲": "urinate",
            "溶": "dissolve, melt",
            "溺": "drown, urinate",
            "溼": "wet, damp",
            "滂": "torrential",
            "滄": "blue-green, cold",
            "滅": "extinguish, destroy",
            "滋": "nourish, grow",
            "滌": "wash, cleanse",
            "滓": "dregs, sediment",
            "滔": "overflow, excessive",
            "滕": "Teng (surname)",
            "滙": "converge, remit",
            "滚": "roll, boil",
            "滝": "waterfall",
            "滟": "sparkle",
            "滢": "clear, pure",
            "滤": "filter, strain",
            "滥": "excessive, flood",
            "滨": "shore, bank",
            "滩": "beach, shoal",
            "滬": "Shanghai",
            "滯": "stagnate, block",
            "滲": "seep, ooze",
            "滴": "drip, drop",
            "滷": "brine, salt",
            "滸": "shore, bank",
            "滾": "roll, boil",
            "滿": "full, satisfied",
            "漁": "fishing",
            "漂": "float, drift",
            "漆": "lacquer, paint",
            "漉": "strain, filter",
            "漏": "leak, escape",
            "演": "perform, deduce",
            "漓": "drip, trickle",
            "漕": "transport grain",
            "漠": "desert, indifferent",
            "漢": "Han Chinese",
            "漣": "ripples",
            "漩": "whirlpool",
            "漪": "ripples",
            "漫": "overflow, unrestrained",
            "漬": "soak, pickle",
            "漱": "rinse, gargle",
            "漲": "rise, swell",
            "漳": "Zhang river",
            "漸": "gradually",
            "漾": "ripple, overflow",
            "漿": "thick liquid",
            "潑": "pour, splash",
            "潔": "clean, pure",
            "潘": "Pan (surname)",
            "潛": "hide, latent",
            "潤": "moist, smooth",
            "潦": "flood, careless",
            "潭": "deep pool",
            "潮": "tide, damp",
            "潰": "burst, collapse",
            "潴": "pool, stagnant",
            "潸": "tears flowing",
            "潺": "murmur",
            "澀": "astringent",
            "澄": "clear, settle",
            "澆": "pour, water",
            "澈": "clear, transparent",
            "澎": "surge",
            "澗": "mountain stream",
            "澡": "bathe, wash",
            "澤": "marsh, favor",
            "澱": "sediment",
            "澳": "bay, Macao",
            "澹": "tranquil, indifferent",
            "激": "arouse, violent",
            "濁": "turbid, muddy",
            "濃": "thick, strong",
            "濆": "bank, shore",
            "濇": "astringent",
            "濑": "rapids",
            "濒": "border, near",
            "濕": "wet, damp",
            "濘": "muddy",
            "濛": "drizzle, dim",
            "濟": "help, cross",
            "濠": "moat",
            "濡": "moisten, wet",
            "濤": "large waves",
            "濫": "excessive, flood",
            "濬": "dredge, deep",
            "濮": "Pu river",
            "濯": "wash, cleanse",
            "濰": "Wei river",
            "濱": "shore, bank",
            "濳": "hide, submerge",
            "濵": "shore",
            "濶": "wide, broad",
            "濺": "splash",
            "濾": "filter",
            "瀁": "ripples",
            "瀅": "clear",
            "瀆": "ditch, profane",
            "瀉": "flow, diarrhea",
            "瀋": "Shenyang",
            "瀌": "drizzle",
            "瀏": "clear, flow",
            "瀑": "waterfall",
            "瀕": "border, near",
            "瀚": "vast",
            "瀛": "sea, ocean",
            "瀝": "drip, trickle",
            "瀞": "clear, tranquil",
            "瀟": "Xiao river",
            "瀠": "flow around",
            "瀣": "dew",
            "瀦": "pool, stagnant",
            "瀧": "rapids",
            "瀨": "rapids",
            "瀬": "rapids",
            "瀰": "overflow",
            "瀲": "ripples",
            "瀵": "spring",
            "瀹": "boil, soak",
            "瀺": "splash",
            "瀾": "large waves",
            "灃": "Feng river",
            "灋": "law",
            "灌": "irrigate, pour",
            "灏": "vast",
            "灑": "sprinkle",
            "灔": "overflow",
            "灕": "Li river",
            "灘": "beach, shoal",
            "灝": "vast",
            "灞": "Ba river",
            "灣": "bay, gulf",
            "灤": "Luan river",
            "灥": "three springs",
            "灩": "sparkle",
            "灬": "fire radical",
            "灭": "extinguish",
            "灮": "light",
            "灯": "lamp, light",
            "灰": "ash, gray",
            "灵": "spirit, soul",
            "灶": "stove, kitchen",
            "灼": "burn, cauterize",
            "災": "disaster",
            "灾": "disaster",
            "灿": "brilliant",
            "炀": "roast, Yang",
            "炁": "qi, breath",
            "炅": "bright, Jiong",
            "炆": "simmer",
            "炉": "stove, furnace",
            "炊": "cook",
            "炎": "inflammation, flame",
            "炒": "stir-fry",
            "炔": "alkyne",
            "炕": "kang (heated bed)",
            "炖": "stew",
            "炙": "roast, broil",
            "炜": "brilliant",
            "炝": "quick-fry",
            "炤": "shine",
            "炫": "dazzle",
            "炬": "torch",
            "炭": "charcoal",
            "炮": "cannon, prepare",
            "炯": "bright",
            "炰": "roast",
            "炱": "soot",
            "炳": "bright, manifest",
            "炷": "wick",
            "炸": "explode, fry",
            "点": "point, dot",
            "為": "do, be",
            "炻": "stoneware",
            "炼": "refine, smelt",
            "炽": "blazing",
            "烀": "stew",
            "烁": "sparkle",
            "烂": "rotten, cooked",
            "烃": "hydrocarbon",
            "烈": "intense, fierce",
            "烊": "melt, smelt",
            "烏": "crow, black",
            "烕": "extinguish",
            "烖": "disaster",
            "烘": "bake, dry",
            "烙": "brand, bake",
            "烚": "boil",
            "烛": "candle",
            "烜": "brilliant",
            "烝": "steam, many",
            "烟": "smoke, tobacco",
            "烤": "roast, bake",
            "烦": "vexed, annoyed",
            "烧": "burn, fever",
            "烨": "bright",
            "烩": "braise",
            "烫": "scald, hot",
            "烬": "ashes, cinders",
            "烯": "alkene",
            "烱": "bright",
            "烴": "hydrocarbon",
            "烷": "alkane",
            "烹": "boil, cook",
            "烺": "bright",
            "烽": "beacon fire",
            "焄": "fragrant",
            "焅": "dry",
            "焉": "how, where",
            "焊": "weld, solder",
            "焌": "scorch",
            "焐": "warm",
            "焓": "enthalpy",
            "焔": "flame",
            "焕": "brilliant",
            "焖": "braise, stew",
            "焗": "bake",
            "焘": "cover, protect",
            "焙": "bake, roast",
            "焚": "burn",
            "焜": "brilliant",
            "焠": "temper, quench",
            "無": "not have, without",
            "焢": "bake",
            "焦": "burnt, anxious",
            "焫": "burn",
            "焮": "red-hot",
            "焯": "scald briefly",
            "焰": "flame",
            "焱": "flames",
            "然": "so, correct",
            "焿": "thick soup",
            "煅": "calcine",
            "煆": "calcine",
            "煇": "brilliant",
            "煉": "refine, smelt",
            "煊": "warm",
            "煌": "brilliant",
            "煎": "decoct, fry",
            "煑": "boil, cook",
            "煒": "brilliant",
            "煕": "bright, prosperous",
            "煖": "warm",
            "煗": "warm",
            "煙": "smoke, tobacco",
            "煚": "brilliant",
            "煜": "bright, shine",
            "煞": "evil spirit, very",
            "煠": "boil",
            "煢": "alone",
            "煤": "coal",
            "煥": "brilliant",
            "煦": "warm, kind",
            "照": "shine, photo",
            "煨": "simmer",
            "煩": "vexed, annoyed",
            "煬": "roast, Yang",
            "煮": "boil, cook",
            "煯": "dry by fire",
            "煰": "soot",
            "煲": "pot, cook",
            "煳": "burnt, scorched",
            "煴": "warm",
            "煸": "stir-fry",
            "煺": "fade",
            "煻": "hot",
            "煽": "fan, incite",
            "煾": "warm",
            "熀": "brilliant",
            "熁": "warm",
            "熄": "extinguish",
            "熅": "warm",
            "熇": "hot",
            "熈": "bright, prosperous",
            "熊": "bear",
            "熏": "smoke, fumigate",
            "熒": "glimmer",
            "熔": "melt, fuse",
            "熕": "cannon",
            "熖": "flame",
            "熗": "quick-fry",
            "熘": "quick-fry",
            "熙": "bright, prosperous",
            "熛": "blaze",
            "熝": "dry",
            "熟": "ripe, cooked",
            "熠": "glitter",
            "熢": "beacon fire",
            "熥": "warm up",
            "熨": "iron, press",
            "熬": "boil, endure",
            "熯": "dry, scorch",
            "熰": "smoke",
            "熱": "hot, heat",
            "熲": "brilliant",
            "熳": "overflow",
            "熴": "smoke",
            "熵": "entropy",
            "熸": "extinguish",
            "熹": "bright",
            "熺": "bright",
            "熾": "blazing",
            "燀": "stew",
            "燁": "bright",
            "燂": "scald",
            "燃": "burn, ignite",
            "燄": "flame",
            "燈": "lamp, light",
            "燉": "stew",
            "燊": "flourishing",
            "燋": "burnt",
            "燎": "burn, singe",
            "燐": "phosphorus",
            "燒": "burn, fever",
            "燓": "burn",
            "燔": "roast, burn",
            "燕": "swallow, Yan",
            "燖": "scald",
            "燗": "warm sake",
            "燙": "scald, hot",
            "燚": "flames",
            "燜": "braise, stew",
            "營": "camp, manage",
            "燠": "warm, hot",
            "燥": "dry",
            "燦": "brilliant",
            "燧": "fire drill",
            "燬": "destroy by fire",
            "燭": "candle",
            "燮": "harmonize",
            "燴": "braise",
            "燵": "kotatsu",
            "燶": "burnt",
            "燸": "warm",
            "燹": "prairie fire",
            "燻": "smoke, fumigate",
            "燼": "ashes, cinders",
            "燾": "cover, protect",
            "燿": "shine, dazzle",
            "爀": "brilliant",
            "爆": "explode",
            "爇": "burn",
            "爊": "roast",
            "爌": "braise",
            "爍": "sparkle",
            "爏": "river name",
            "爐": "stove, furnace",
            "爓": "burn",
            "爕": "harmonize",
            "爘": "brilliant",
            "爚": "brilliant",
            "爛": "rotten, cooked",
            "爝": "torch",
            "爞": "bright",
            "爟": "beacon fire",
            "爨": "cook, kitchen",
            "爪": "claw, nail",
            "爫": "claw radical",
            "爬": "crawl, climb",
            "爭": "contend, strive",
        }

    def _load_radical_meanings(self) -> dict[str, str]:
        """Load meanings for common Chinese radicals."""
        return {
            # Common Kangxi radicals
            "一": "one (horizontal line)",
            "丨": "line (vertical line)",
            "丶": "dot",
            "丿": "slash",
            "乙": "second, bent",
            "亅": "hook",
            "二": "two",
            "亠": "lid, cover",
            "人": "person",
            "亻": "person (radical)",
            "儿": "legs",
            "入": "enter",
            "八": "eight, divide",
            "冂": "down box",
            "冖": "cover",
            "冫": "ice",
            "几": "table",
            "凵": "container",
            "刀": "knife",
            "刂": "knife (radical)",
            "力": "power, strength",
            "勹": "wrap",
            "匕": "spoon",
            "匚": "box",
            "匸": "hiding enclosure",
            "十": "ten",
            "卜": "divination",
            "卩": "seal",
            "厂": "cliff",
            "厶": "private",
            "又": "again, right hand",
            "口": "mouth",
            "囗": "enclosure",
            "土": "earth",
            "士": "scholar",
            "夂": "go slowly",
            "夊": "go",
            "夕": "evening",
            "大": "big",
            "女": "woman",
            "子": "child",
            "宀": "roof",
            "寸": "inch",
            "小": "small",
            "尢": "lame",
            "尸": "corpse",
            "屮": "sprout",
            "山": "mountain",
            "巛": "river",
            "川": "river",
            "工": "work",
            "己": "self",
            "巾": "turban, cloth",
            "干": "dry",
            "幺": "tiny, thread",
            "广": "shelter",
            "廴": "long stride",
            "廾": "two hands",
            "弋": "shoot",
            "弓": "bow",
            "彐": "snout",
            "彡": "bristle, hair",
            "彳": "step",
            "心": "heart",
            "忄": "heart (radical)",
            "戈": "halberd",
            "戶": "door",
            "手": "hand",
            "扌": "hand (radical)",
            "支": "branch",
            "攴": "tap",
            "攵": "strike (radical)",
            "文": "script, culture",
            "斗": "dipper",
            "斤": "axe",
            "方": "square, direction",
            "无": "not have",
            "日": "sun, day",
            "曰": "say",
            "月": "moon, month",
            "木": "wood, tree",
            "欠": "lack, yawn",
            "止": "stop",
            "歹": "death, evil",
            "殳": "weapon",
            "毋": "do not",
            "比": "compare",
            "毛": "fur, hair",
            "氏": "clan",
            "气": "qi, air",
            "氣": "qi, air",
            "水": "water",
            "氵": "water (radical)",
            "火": "fire",
            "灬": "fire (radical)",
            "爪": "claw",
            "爫": "claw (radical)",
            "父": "father",
            "爻": "trigram",
            "爿": "split wood",
            "片": "slice",
            "牙": "tooth",
            "牛": "cow, ox",
            "牜": "cow (radical)",
            "犬": "dog",
            "犭": "dog (radical)",
            "玄": "dark, mysterious",
            "玉": "jade",
            "王": "king",
            "瓜": "melon",
            "瓦": "tile",
            "甘": "sweet",
            "生": "life, birth",
            "用": "use",
            "田": "field",
            "疋": "bolt of cloth",
            "疒": "sickness",
            "癶": "footsteps",
            "白": "white",
            "皮": "skin",
            "皿": "dish",
            "目": "eye",
            "矛": "spear",
            "矢": "arrow",
            "石": "stone",
            "示": "show, spirit",
            "礻": "spirit (radical)",
            "禸": "track",
            "禾": "grain",
            "穴": "cave",
            "立": "stand",
            "竹": "bamboo",
            "⺮": "bamboo (radical)",
            "米": "rice",
            "糸": "silk",
            "糹": "silk (radical)",
            "缶": "jar",
            "网": "net",
            "羊": "sheep",
            "羽": "feather",
            "老": "old",
            "而": "and, yet",
            "耒": "plow",
            "耳": "ear",
            "聿": "brush",
            "肉": "meat, flesh",
            "月": "meat/moon (radical)",
            "臣": "minister",
            "自": "self",
            "至": "arrive",
            "臼": "mortar",
            "舌": "tongue",
            "舛": "oppose",
            "舟": "boat",
            "艮": "stopping",
            "色": "color",
            "艸": "grass",
            "艹": "grass (radical)",
            "虍": "tiger",
            "虫": "insect",
            "血": "blood",
            "行": "go, walk",
            "衣": "clothes",
            "衤": "clothes (radical)",
            "襾": "cover",
            "見": "see",
            "角": "horn",
            "言": "speech",
            "訁": "speech (radical)",
            "谷": "valley",
            "豆": "bean",
            "豕": "pig",
            "豸": "badger",
            "貝": "shell, money",
            "赤": "red",
            "走": "run",
            "足": "foot",
            "⻊": "foot (radical)",
            "身": "body",
            "車": "cart, vehicle",
            "辛": "bitter, spicy",
            "辰": "morning, time",
            "辵": "walk",
            "⻌": "walk (radical)",
            "邑": "city",
            "阝": "mound/city (radical)",
            "酉": "wine vessel",
            "釆": "distinguish",
            "里": "village, mile",
            "金": "metal, gold",
            "釒": "metal (radical)",
            "長": "long",
            "門": "gate",
            "阜": "mound",
            "隶": "slave",
            "隹": "short-tailed bird",
            "雨": "rain",
            "青": "blue, green",
            "非": "not, wrong",
            "面": "face",
            "革": "leather",
            "韋": "tanned leather",
            "韭": "leek",
            "音": "sound",
            "頁": "head, page",
            "風": "wind",
            "飛": "fly",
            "食": "food, eat",
            "飠": "food (radical)",
            "首": "head",
            "香": "fragrant",
            "馬": "horse",
            "骨": "bone",
            "高": "tall, high",
            "髟": "long hair",
            "鬥": "fight",
            "鬯": "sacrificial wine",
            "鬲": "cauldron",
            "鬼": "ghost, demon",
            "魚": "fish",
            "鳥": "bird",
            "鹵": "salt",
            "鹿": "deer",
            "麥": "wheat",
            "麻": "hemp, numb",
            "黃": "yellow",
            "黍": "millet",
            "黑": "black",
            "黹": "embroidery",
            "黽": "frog",
            "鼎": "tripod",
            "鼓": "drum",
            "鼠": "rat, mouse",
            "鼻": "nose",
            "齊": "even, uniform",
            "齒": "tooth",
            "龍": "dragon",
            "龜": "turtle",
            "龠": "flute",
        }

    def get_unicode_info(self, char: str) -> dict:
        """Get Unicode information for a character."""
        return {
            "unicode": f"U+{ord(char):04X}",
            "decimal": ord(char),
            "name": unicodedata.name(char, "UNKNOWN"),
            "category": unicodedata.category(char),
        }

    def get_pinyin(self, char: str) -> list[str]:
        """Get pinyin pronunciation(s) for a character."""
        if self.has_pypinyin:
            # Get pinyin with tone marks
            result = self.pypinyin([char], style=self.pinyin_style.TONE)
            return result[0] if result else [""]
        return [""]

    def get_character_meanings(self, char: str) -> list[str]:
        """Get English meanings/definitions for a character."""
        # Check basic meanings dictionary first
        if char in self.basic_meanings:
            return [self.basic_meanings[char]]

        # If not in basic dictionary, return placeholder
        return ["(meaning not in dictionary)"]

    def get_radical_info(self, char: str) -> dict:
        """Get radical information and components for a character."""
        radical_info = {"radical": "", "radical_meaning": "", "components": []}

        if self.has_cjkradlib and self.decomposer:
            try:
                # Get character sub-components (parts that make up the character)
                sub_components = self.decomposer.get_sub(char)
                if sub_components:
                    # Filter to only common/recognizable components
                    radical_info["components"] = [
                        c for c in sub_components if ord(c) < 0x3000 or (0x4E00 <= ord(c) <= 0x9FFF)
                    ]

                    # The first component is often the radical
                    if radical_info["components"]:
                        radical_info["radical"] = radical_info["components"][0]
                        # Try to get meaning of radical from radical dictionary first
                        if radical_info["radical"] in self.radical_meanings:
                            radical_info["radical_meaning"] = self.radical_meanings[radical_info["radical"]]
                        # Then try basic meanings dictionary
                        elif radical_info["radical"] in self.basic_meanings:
                            radical_info["radical_meaning"] = self.basic_meanings[radical_info["radical"]]

            except Exception:
                pass

        return radical_info

    def analyze_character(self, char: str) -> dict:
        """Perform comprehensive analysis of a single character."""
        if char in self.character_data:
            return self.character_data[char]

        # Get stroke order information
        stroke_info = self.stroke_order.get_stroke_order_info(char)

        # Get character meanings
        meanings = self.get_character_meanings(char)

        # Get radical information
        radical_info = self.get_radical_info(char)

        analysis = {
            "character": char,
            "unicode_info": self.get_unicode_info(char),
            "pinyin": self.get_pinyin(char),
            "radical_info": radical_info,
            "meanings": meanings,
            "etymology": "",  # Would be populated from etymology database
            "stroke_order": stroke_info,
            "compounds": [],  # Common compounds containing this character
        }

        self.character_data[char] = analysis
        return analysis

    def analyze_term(self, hanzi: str, pinyin: str = "") -> dict:
        """Analyze a multi-character term."""
        characters = []

        for char in hanzi:
            if ord(char) >= 0x4E00 and ord(char) <= 0x9FFF:
                char_analysis = self.analyze_character(char)
                characters.append(char_analysis)

        return {"full_term": hanzi, "full_pinyin": pinyin, "character_count": len(characters), "characters": characters}


class FlashcardGenerator:
    """Generate flashcards in various formats."""

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_anki_csv(
        self,
        terms: dict[str, dict],
        character_analyses: dict[str, dict],
        output_file: str = "tcm_chinese_flashcards.csv",
    ) -> None:
        """Generate Anki-compatible CSV file with stroke order links."""
        import csv

        output_path = self.output_dir / output_file

        with open(output_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter="\t")

            # Header
            writer.writerow(
                [
                    "Hanzi",
                    "Pinyin",
                    "English",
                    "Category",
                    "Character Breakdown",
                    "Meanings & Radicals",
                    "Stroke Order Links",
                    "Tags",
                ]
            )

            for hanzi, term_data in sorted(terms.items()):
                pinyin = term_data.get("pinyin", "")
                english = term_data.get("english", "")
                category = term_data.get("category", "")

                # Build character breakdown with stroke order
                char_breakdown = []
                meanings_radicals = []
                stroke_links = []

                for char in hanzi:
                    if char in character_analyses:
                        char_info = character_analyses[char]
                        char_pinyin = char_info.get("pinyin", [""])[0]
                        char_breakdown.append(f"{char} ({char_pinyin})")

                        # Add meanings and radical info
                        meanings = char_info.get("meanings", [])
                        radical_info = char_info.get("radical_info", {})
                        radical = radical_info.get("radical", "")
                        components = radical_info.get("components", [])

                        meaning_str = meanings[0] if meanings else ""
                        radical_str = f"[radical: {radical}]" if radical else ""
                        components_str = f"[components: {', '.join(components)}]" if components else ""

                        char_detail = f"{char}: {meaning_str} {radical_str} {components_str}".strip()
                        meanings_radicals.append(char_detail)

                        # Add stroke order link
                        stroke_info = char_info.get("stroke_order", {})
                        if stroke_info:
                            stroke_url = stroke_info.get("strokeorder_url", "")
                            stroke_links.append(f'<a href="{stroke_url}">{char}</a>')

                breakdown_str = " + ".join(char_breakdown)
                meanings_radicals_str = " | ".join(meanings_radicals)
                stroke_links_html = " ".join(stroke_links)

                tags = f"TCM::{category}"

                writer.writerow(
                    [hanzi, pinyin, english, category, breakdown_str, meanings_radicals_str, stroke_links_html, tags]
                )

        print(f"✓ Anki CSV generated: {output_path}")

    def generate_json_database(
        self,
        terms: dict[str, dict],
        character_analyses: dict[str, dict],
        output_file: str = "tcm_chinese_database.json",
    ) -> None:
        """Generate comprehensive JSON database."""
        output_path = self.output_dir / output_file

        database = {
            "metadata": {
                "version": "1.0",
                "total_terms": len(terms),
                "total_characters": len(character_analyses),
                "generated_date": "",
            },
            "terms": terms,
            "characters": character_analyses,
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(database, f, ensure_ascii=False, indent=2)

        print(f"✓ JSON database generated: {output_path}")

    def generate_markdown_flashcards(
        self,
        terms: dict[str, dict],
        character_analyses: dict[str, dict],
        output_file: str = "tcm_chinese_flashcards.md",
    ) -> None:
        """Generate markdown flashcard file."""
        output_path = self.output_dir / output_file

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# TCM Chinese Character Flashcards\n\n")
            f.write("Generated from TCM Knowledge Base\n\n")
            f.write("---\n\n")

            # Group by category
            by_category = defaultdict(list)
            for hanzi, term_data in terms.items():
                by_category[term_data["category"]].append((hanzi, term_data))

            for category in sorted(by_category.keys()):
                f.write(f"## {category.replace('_', ' ').title()}\n\n")

                for hanzi, term_data in sorted(by_category[category]):
                    f.write(f"### {hanzi}\n\n")

                    if term_data.get("pinyin"):
                        f.write(f"**Pinyin:** {term_data['pinyin']}\n\n")

                    if term_data.get("english"):
                        f.write(f"**English:** {term_data['english']}\n\n")

                    if term_data.get("additional_info"):
                        f.write(f"**Additional:** {term_data['additional_info']}\n\n")

                    # Character breakdown
                    f.write("**Character Breakdown:**\n\n")

                    for char in hanzi:
                        if char in character_analyses:
                            char_info = character_analyses[char]
                            char_pinyin = char_info.get("pinyin", [""])[0]
                            unicode_info = char_info.get("unicode_info", {})
                            radical_info = char_info.get("radical_info", {})

                            f.write(f"- **{char}** ({char_pinyin})\n")
                            f.write(f"  - Unicode: {unicode_info.get('unicode', '')}\n")

                            if char_info.get("meanings"):
                                meanings_list = char_info["meanings"][:3]  # First 3 meanings
                                f.write(f"  - Meanings: {', '.join(meanings_list)}\n")

                            # Add radical information
                            if radical_info.get("radical"):
                                f.write(f"  - Radical: {radical_info['radical']}\n")

                            if radical_info.get("components"):
                                components = ", ".join(radical_info["components"][:5])  # First 5 components
                                f.write(f"  - Components: {components}\n")

                            f.write("\n")

                    f.write("---\n\n")

        print(f"✓ Markdown flashcards generated: {output_path}")

    def generate_character_list(
        self, character_analyses: dict[str, dict], output_file: str = "tcm_character_list.txt"
    ) -> None:
        """Generate simple list of all unique characters with meanings and radicals."""
        output_path = self.output_dir / output_file

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# TCM Chinese Characters - Complete List\n\n")
            f.write(f"Total unique characters: {len(character_analyses)}\n\n")
            f.write("Format: Character | Pinyin | Unicode | Meaning | Radical | Components\n\n")

            for char in sorted(character_analyses.keys()):
                char_info = character_analyses[char]
                pinyin = char_info.get("pinyin", [""])[0]
                unicode_info = char_info.get("unicode_info", {})
                meanings = char_info.get("meanings", [])
                radical_info = char_info.get("radical_info", {})

                meaning = meanings[0] if meanings else ""
                radical = radical_info.get("radical", "")
                components = ", ".join(radical_info.get("components", [])[:3])  # First 3 components

                f.write(f"{char}\t{pinyin}\t{unicode_info.get('unicode', '')}\t{meaning}\t{radical}\t{components}\n")

        print(f"✓ Character list generated: {output_path}")

    def generate_obsidian_flashcards(
        self,
        terms: dict[str, dict],
        character_analyses: dict[str, dict],
        output_dir: str = "Flashcards/Chinese_Characters",
    ) -> None:
        """Generate Obsidian Spaced Repetition flashcards grouped by category."""
        from collections import defaultdict
        from datetime import datetime

        flashcard_dir = self.output_dir.parent / output_dir
        flashcard_dir.mkdir(parents=True, exist_ok=True)

        # Group terms by category
        by_category = defaultdict(list)
        for hanzi, term_data in terms.items():
            category = term_data.get("category", "uncategorized")
            by_category[category].append((hanzi, term_data))

        # Also group herbs by herb category and points by channel
        by_herb_category = defaultdict(list)
        by_point_channel = defaultdict(list)

        for hanzi, term_data in terms.items():
            category = term_data.get("category", "")
            sources = term_data.get("sources", [])

            if category == "herb" and sources:
                # Try to extract herb category from source file
                for source in sources:
                    if "TCM_Herbs" in source:
                        # Read the herb file to get category
                        try:
                            with open(source, encoding="utf-8") as f:
                                content = f.read()
                                # Extract category from frontmatter
                                import re

                                match = re.search(r"category:\s*\n\s*-\s*(.+)", content)
                                if match:
                                    herb_cat = match.group(1).strip()
                                    by_herb_category[herb_cat].append((hanzi, term_data))
                                    break
                        except:
                            pass

            elif category == "acupuncture_point":
                # Extract channel from point code (e.g., "BL-1" -> "Bladder", "ST-36" -> "Stomach")
                additional_info = term_data.get("additional_info", "")
                if additional_info and "-" in additional_info:
                    # Map point codes to channel names
                    channel_map = {
                        "BL": "Bladder",
                        "B": "Bladder",
                        "ST": "Stomach",
                        "S": "Stomach",
                        "SP": "Spleen",
                        "HT": "Heart",
                        "H": "Heart",
                        "SI": "Small Intestine",
                        "KI": "Kidney",
                        "K": "Kidney",
                        "PC": "Pericardium",
                        "P": "Pericardium",
                        "SJ": "San Jiao",
                        "TH": "San Jiao",
                        "TE": "San Jiao",
                        "GB": "Gall Bladder",
                        "G": "Gall Bladder",
                        "LV": "Liver",
                        "LIV": "Liver",
                        "LU": "Lung",
                        "L": "Lung",
                        "LI": "Large Intestine",
                        "REN": "Ren",
                        "CV": "Ren",
                        "DU": "Du",
                        "GV": "Du",
                    }

                    code_prefix = additional_info.split("-")[0].upper()
                    if code_prefix in channel_map:
                        channel = channel_map[code_prefix]
                        by_point_channel[channel].append((hanzi, term_data))

        today = datetime.now().strftime("%Y-%m-%d")

        # Generate flashcard for ALL unique characters
        self._generate_all_characters_flashcard(character_analyses, flashcard_dir, today)

        # Generate flashcards by main category (herbs, points, etc.)
        for category, items in by_category.items():
            if items:
                self._generate_category_flashcard(category, items, character_analyses, flashcard_dir, today)

        # Generate flashcards by herb category
        for herb_cat, items in by_herb_category.items():
            if items:
                self._generate_herb_category_flashcard(herb_cat, items, character_analyses, flashcard_dir, today)

        # Generate flashcards by point channel
        for channel, items in by_point_channel.items():
            if items:
                self._generate_point_channel_flashcard(channel, items, character_analyses, flashcard_dir, today)

        print(f"✓ Obsidian flashcards generated: {flashcard_dir}")

    def _generate_all_characters_flashcard(
        self, character_analyses: dict[str, dict], output_dir: Path, today: str
    ) -> None:
        """Generate a single flashcard file with all unique characters."""
        output_path = output_dir / "Flashcards_All_Unique_Characters.md"

        with open(output_path, "w", encoding="utf-8") as f:
            # Frontmatter
            f.write("---\n")
            f.write("material_type: flashcard_collection\n")
            f.write("topic: TCM Chinese Characters\n")
            f.write("category: All Unique Characters\n")
            f.write(f"total_cards: {len(character_analyses)}\n")
            f.write(f"created: {today}\n")
            f.write("tags:\n")
            f.write("  - flashcards\n")
            f.write("  - chinese\n")
            f.write("  - characters\n")
            f.write("---\n\n")

            f.write("# TCM Chinese Characters: All Unique Characters\n\n")
            f.write(f"**Total Cards:** {len(character_analyses)}\n")
            f.write(f"**Created:** {today}\n\n")
            f.write("---\n\n")

            # Generate cards for each character
            for char in sorted(character_analyses.keys()):
                char_info = character_analyses[char]
                self._write_character_card(f, char, char_info)

    def _generate_category_flashcard(
        self,
        category: str,
        items: list[tuple[str, dict]],
        character_analyses: dict[str, dict],
        output_dir: Path,
        today: str,
    ) -> None:
        """Generate flashcard file for a main category (herbs, points, etc.)."""
        category_name = category.replace("_", " ").title()
        filename = f"Flashcards_{category.replace(' ', '_')}_Characters.md"
        output_path = output_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            # Frontmatter
            f.write("---\n")
            f.write("material_type: flashcard_collection\n")
            f.write("topic: TCM Chinese Characters\n")
            f.write(f"category: {category_name}\n")
            f.write(f"total_cards: {len(items)}\n")
            f.write(f"created: {today}\n")
            f.write("tags:\n")
            f.write("  - flashcards\n")
            f.write("  - chinese\n")
            f.write(f"  - {category}\n")
            f.write("---\n\n")

            f.write(f"# TCM Chinese Characters: {category_name}\n\n")
            f.write(f"**Total Cards:** {len(items)}\n")
            f.write(f"**Category:** {category_name}\n")
            f.write(f"**Created:** {today}\n\n")
            f.write("---\n\n")

            # Generate cards for each term
            for hanzi, term_data in sorted(items):
                self._write_term_card(f, hanzi, term_data, character_analyses)

    def _generate_herb_category_flashcard(
        self,
        herb_category: str,
        items: list[tuple[str, dict]],
        character_analyses: dict[str, dict],
        output_dir: Path,
        today: str,
    ) -> None:
        """Generate flashcard file for a specific herb category."""
        safe_name = herb_category.replace("/", "_").replace(" ", "_")
        filename = f"Flashcards_Herbs_{safe_name}_Characters.md"
        output_path = output_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            # Frontmatter
            f.write("---\n")
            f.write("material_type: flashcard_collection\n")
            f.write("topic: TCM Chinese Characters\n")
            f.write("category: Herbs\n")
            f.write(f"herb_category: {herb_category}\n")
            f.write(f"total_cards: {len(items)}\n")
            f.write(f"created: {today}\n")
            f.write("tags:\n")
            f.write("  - flashcards\n")
            f.write("  - chinese\n")
            f.write("  - herbs\n")
            f.write(f"  - {safe_name}\n")
            f.write("---\n\n")

            f.write(f"# TCM Chinese Characters: {herb_category}\n\n")
            f.write(f"**Total Cards:** {len(items)}\n")
            f.write(f"**Herb Category:** {herb_category}\n")
            f.write(f"**Created:** {today}\n\n")
            f.write("---\n\n")

            # Generate cards for each herb
            for hanzi, term_data in sorted(items):
                self._write_term_card(f, hanzi, term_data, character_analyses)

    def _generate_point_channel_flashcard(
        self,
        channel: str,
        items: list[tuple[str, dict]],
        character_analyses: dict[str, dict],
        output_dir: Path,
        today: str,
    ) -> None:
        """Generate flashcard file for a specific acupuncture point channel."""
        safe_name = channel.replace(" ", "_")
        filename = f"Flashcards_Points_{safe_name}_Characters.md"
        output_path = output_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            # Frontmatter
            f.write("---\n")
            f.write("material_type: flashcard_collection\n")
            f.write("topic: TCM Chinese Characters\n")
            f.write("category: Acupuncture Points\n")
            f.write(f"channel: {channel}\n")
            f.write(f"total_cards: {len(items)}\n")
            f.write(f"created: {today}\n")
            f.write("tags:\n")
            f.write("  - flashcards\n")
            f.write("  - chinese\n")
            f.write("  - acupoints\n")
            f.write(f"  - {safe_name}\n")
            f.write("---\n\n")

            f.write(f"# TCM Chinese Characters: {channel} Channel Points\n\n")
            f.write(f"**Total Cards:** {len(items)}\n")
            f.write(f"**Channel:** {channel}\n")
            f.write(f"**Created:** {today}\n\n")
            f.write("---\n\n")

            # Generate cards for each point
            for hanzi, term_data in sorted(items):
                self._write_term_card(f, hanzi, term_data, character_analyses)

    def _write_character_card(self, f, char: str, char_info: dict) -> None:
        """Write a single character flashcard in Obsidian SR format."""
        pinyin = char_info.get("pinyin", [""])[0]
        meanings = char_info.get("meanings", [])
        radical_info = char_info.get("radical_info", {})
        unicode_info = char_info.get("unicode_info", {})

        # Card front (question)
        f.write(f"# **{char}** ({pinyin})\n")
        f.write("## What is the meaning, radical, and components of this character?\n")
        f.write("?\n")

        # Card back (answer)
        if meanings:
            f.write(f"**Meaning:** {meanings[0]}\n")
        f.write(f"**Unicode:** {unicode_info.get('unicode', '')}\n")

        if radical_info.get("radical"):
            radical = radical_info["radical"]
            radical_meaning = radical_info.get("radical_meaning", "")
            if radical_meaning:
                f.write(f"**Radical:** {radical} ({radical_meaning})\n")
            else:
                f.write(f"**Radical:** {radical}\n")

        if radical_info.get("components"):
            components = ", ".join(radical_info["components"][:5])
            f.write(f"**Components:** {components}\n")

        # Stroke order link
        stroke_info = char_info.get("stroke_order", {})
        if stroke_info:
            stroke_url = stroke_info.get("strokeorder_url", "")
            if stroke_url:
                f.write(f"**Stroke Order:** [View on StrokeOrder.com]({stroke_url})\n")

        f.write("<!--SR:!2025-11-10,3,250-->\n\n")
        f.write("---\n\n")

    def _write_term_card(self, f, hanzi: str, term_data: dict, character_analyses: dict[str, dict]) -> None:
        """Write a term flashcard (multi-character word) in Obsidian SR format."""
        pinyin = term_data.get("pinyin", "")
        english = term_data.get("english", "")
        additional_info = term_data.get("additional_info", "")

        # Card front (question)
        f.write(f"# **{hanzi}**")
        if pinyin:
            f.write(f" · {pinyin}")
        if english:
            f.write(f" · *{english}*")
        f.write("\n")
        f.write("## What are the individual characters and their meanings in this term?\n")
        f.write("?\n")

        # Card back (answer) - character breakdown
        for char in hanzi:
            if char in character_analyses:
                char_info = character_analyses[char]
                char_pinyin = char_info.get("pinyin", [""])[0]
                meanings = char_info.get("meanings", [])
                radical_info = char_info.get("radical_info", {})

                f.write(f"**{char}** ({char_pinyin})")
                if meanings:
                    f.write(f" - {meanings[0]}")
                f.write("\n")

                if radical_info.get("radical"):
                    radical = radical_info["radical"]
                    radical_meaning = radical_info.get("radical_meaning", "")
                    if radical_meaning:
                        f.write(f"  - Radical: {radical} ({radical_meaning})")
                    else:
                        f.write(f"  - Radical: {radical}")
                    f.write("\n")

                if radical_info.get("components"):
                    components = ", ".join(radical_info["components"][:3])
                    f.write(f"  - Components: {components}\n")

                f.write("\n")

        if additional_info:
            f.write(f"**Additional Info:** {additional_info}\n")

        f.write("<!--SR:!2025-11-10,3,250-->\n\n")
        f.write("---\n\n")


def main():
    """Main execution function."""
    print("=" * 60)
    print("TCM Chinese Character Flashcard Generator")
    print("=" * 60)
    print()

    # Get base path
    base_path = Path(__file__).parent.parent

    # Step 1: Extract Chinese terms from knowledge base
    print("Step 1: Extracting Chinese terms from knowledge base...")
    extractor = ChineseCharacterExtractor(str(base_path))
    extractor.scan_all_files()

    # Print statistics
    stats = extractor.get_statistics()
    print("\n" + "=" * 60)
    print("Extraction Statistics")
    print("=" * 60)
    print(f"Total unique terms: {stats['total_terms']}")
    print(f"Total unique characters: {stats['total_characters']}")
    print("\nTerms by category:")
    for category, count in sorted(stats["by_category"].items()):
        print(f"  {category}: {count}")
    print("\nTerms by character count:")
    for count, num_terms in sorted(stats["by_character_count"].items()):
        print(f"  {count} characters: {num_terms} terms")

    # Step 2: Analyze characters
    print("\n" + "=" * 60)
    print("Step 2: Analyzing individual characters...")
    print("=" * 60)

    analyzer = ChineseCharacterAnalyzer()

    # Analyze all unique characters
    for char in extractor.all_characters:
        analyzer.analyze_character(char)

    print(f"✓ Analyzed {len(analyzer.character_data)} unique characters")

    # Step 3: Generate flashcards
    print("\n" + "=" * 60)
    print("Step 3: Generating flashcards...")
    print("=" * 60)

    output_dir = base_path / "anki_exports"
    generator = FlashcardGenerator(str(output_dir))

    # Generate various formats
    generator.generate_anki_csv(extractor.chinese_terms, analyzer.character_data)
    generator.generate_json_database(extractor.chinese_terms, analyzer.character_data)
    generator.generate_markdown_flashcards(extractor.chinese_terms, analyzer.character_data)
    generator.generate_character_list(analyzer.character_data)

    # Generate Obsidian Spaced Repetition flashcards
    generator.generate_obsidian_flashcards(extractor.chinese_terms, analyzer.character_data)

    print("\n" + "=" * 60)
    print("✓ Flashcard generation complete!")
    print("=" * 60)
    print(f"\nOutput files saved to: {output_dir}")
    print("\nGenerated files:")
    print("  1. tcm_chinese_flashcards.csv - Anki import file")
    print("  2. tcm_chinese_database.json - Complete database")
    print("  3. tcm_chinese_flashcards.md - Markdown flashcards")
    print("  4. tcm_character_list.txt - Character reference list")
    print("  5. Flashcards/Chinese_Characters/*.md - Obsidian SR flashcards")
    print("\nObsidian Flashcards:")
    print("  - All unique characters in one deck")
    print("  - Separate decks by herb category")
    print("  - Separate decks by acupuncture point channel")
    print("\nTo import into Anki:")
    print("  1. Open Anki")
    print("  2. File > Import")
    print("  3. Select tcm_chinese_flashcards.csv")
    print("  4. Map fields appropriately")
    print()


if __name__ == "__main__":
    main()
