from django.core.management.base import BaseCommand
from smash_note.models import Character

class Command(BaseCommand):
    help = 'Creates all character data in the database'

    def handle(self, *args, **options):
        characters = [
            {"character_id":1,"character_name":"マリオ","img_path":"images/mario.jpg"},
            {"character_id":2,"character_name":"ドンキーコング","img_path":"images/donkey.jpg"},
            {"character_id":3,"character_name":"リンク","img_path":"images/link.jpg"},
            {"character_id":4,"character_name":"サムス","img_path":"images/samus.jpg"},
            {"character_id":5,"character_name":"ダークサムス","img_path":"images/dark_samus.jpg"},
            {"character_id":6,"character_name":"ヨッシー","img_path":"images/yoshi.jpg"},
            {"character_id":7,"character_name":"カービー","img_path":"images/kirby.jpg"},
            {"character_id":8,"character_name":"フォックス","img_path":"images/fox.jpg"},
            {"character_id":9,"character_name":"ピカチュウ","img_path":"images/pikachu.jpg"},
            {"character_id":10,"character_name":"ルイージ","img_path":"images/luigi.jpg"},
            {"character_id":11,"character_name":"ネス","img_path":"images/ness.jpg"},
            {"character_id":12,"character_name":"CF","img_path":"images/captain_falcon.jpg"},
            {"character_id":13,"character_name":"プリン","img_path":"images/purin.jpg"},
            {"character_id":14,"character_name":"ピーチ","img_path":"images/peach.jpg"},
            {"character_id":15,"character_name":"デイジー","img_path":"images/daisy.jpg"},
            {"character_id":16,"character_name":"クッパ","img_path":"images/koopa.jpg"},
            {"character_id":17,"character_name":"アイスクライマー","img_path":"images/ice_climber.jpg"},
            {"character_id":18,"character_name":"シーク","img_path":"images/sheik.jpg"},
            {"character_id":19,"character_name":"ゼルダ","img_path":"images/zelda.jpg"},
            {"character_id":20,"character_name":"ドクターマリオ","img_path":"images/drmario.jpg"},
            {"character_id":21,"character_name":"ピチュー","img_path":"images/pichu.jpg"},
            {"character_id":22,"character_name":"ファルコ","img_path":"images/falco.jpg"},
            {"character_id":23,"character_name":"マルス","img_path":"images/marth.jpg"},
            {"character_id":24,"character_name":"ルキナ","img_path":"images/lucina.jpg"},
            {"character_id":25,"character_name":"こどもリンク","img_path":"images/young_link.jpg"},
            {"character_id":26,"character_name":"ガノンドロフ","img_path":"images/ganondorf.jpg"},
            {"character_id":27,"character_name":"ミューツー","img_path":"images/mewtwo.jpg"},
            {"character_id":28,"character_name":"ロイ","img_path":"images/roy.jpg"},
            {"character_id":29,"character_name":"クロム","img_path":"images/chrom.jpg"},
            {"character_id":30,"character_name":"ゲーム＆ウォッチ","img_path":"images/game_and_watch.jpg"},
            {"character_id":31,"character_name":"メタナイト","img_path":"images/meta_knight.jpg"},
            {"character_id":32,"character_name":"ピット","img_path":"images/pit.jpg"},
            {"character_id":33,"character_name":"ブラックピット","img_path":"images/black_pit.jpg"},
            {"character_id":34,"character_name":"ゼロスーツサムス","img_path":"images/zero_suit_samus.jpg"},
            {"character_id":35,"character_name":"ワリオ","img_path":"images/wario.jpg"},
            {"character_id":36,"character_name":"スネーク","img_path":"images/snake.jpg"},
            {"character_id":37,"character_name":"アイク","img_path":"images/ike.jpg"},
            {"character_id":38,"character_name":"ポケトレ","img_path":"images/pokemon_trainer.jpg"},
            {"character_id":39,"character_name":"ディディコング","img_path":"images/dd.jpg"},
            {"character_id":40,"character_name":"ルカ","img_path":"images/lucas.jpg"},
            {"character_id":41,"character_name":"ソニック","img_path":"images/sonic.jpg"},
            {"character_id":42,"character_name":"デデデ","img_path":"images/ddd.jpg"},
            {"character_id":43,"character_name":"ピクオリ","img_path":"images/pikumin_and_orimar.jpg"},
            {"character_id":44,"character_name":"ルカリオ","img_path":"images/lucario.jpg"},
            {"character_id":45,"character_name":"ロボット","img_path":"images/robot.jpg"},
            {"character_id":46,"character_name":"トゥーンリンク","img_path":"images/toon_link.jpg"},
            {"character_id":47,"character_name":"ウルフ","img_path":"images/wolf.jpg"},
            {"character_id":48,"character_name":"村人","img_path":"images/murabito.jpg"},
            {"character_id":49,"character_name":"ロックマン","img_path":"images/rockman.jpg"},
            {"character_id":50,"character_name":"フィットレ","img_path":"images/fit_trainer.jpg"},
            {"character_id":51,"character_name":"ロゼチコ","img_path":"images/rose_chiko.jpg"},
            {"character_id":52,"character_name":"リトルマック","img_path":"images/little_mac.jpg"},
            {"character_id":53,"character_name":"ゲッコウガ","img_path":"images/gekkouga.jpg"},
            {"character_id":54,"character_name":"パルテナ","img_path":"images/palutena.jpg"},
            {"character_id":55,"character_name":"パックマン","img_path":"images/pac_man.jpg"},
            {"character_id":56,"character_name":"ルフレ","img_path":"images/reflet.jpg"},
            {"character_id":57,"character_name":"シュルク","img_path":"images/shulk.jpg"},
            {"character_id":58,"character_name":"クッパジュニア","img_path":"images/koopa_jr.jpg"},
            {"character_id":59,"character_name":"ダックハント","img_path":"images/duck_hunt.jpg"},
            {"character_id":60,"character_name":"リュウ","img_path":"images/ryu.jpg"},
            {"character_id":61,"character_name":"ケン","img_path":"images/ken.jpg"},
            {"character_id":62,"character_name":"クラウド","img_path":"images/cloud.jpg"},
            {"character_id":63,"character_name":"カムイ","img_path":"images/kamui.jpg"},
            {"character_id":64,"character_name":"ベヨネッタ","img_path":"images/bayonetta.jpg"},
            {"character_id":65,"character_name":"インクリング","img_path":"images/inkling.jpg"},
            {"character_id":66,"character_name":"リドリー","img_path":"images/ridley.jpg"},
            {"character_id":67,"character_name":"シモン","img_path":"images/simon.jpg"},
            {"character_id":68,"character_name":"リヒター","img_path":"images/richter.jpg"},
            {"character_id":69,"character_name":"キングクルール","img_path":"images/king_k_rool.jpg"},
            {"character_id":70,"character_name":"しずえ","img_path":"images/shizue.jpg"},
            {"character_id":71,"character_name":"ガオガエン","img_path":"images/gaogaen.jpg"},
            {"character_id":72,"character_name":"パックンフラワー","img_path":"images/packun_flower.jpg"},
            {"character_id":73,"character_name":"ジョーカー","img_path":"images/joker.jpg"},
            {"character_id":74,"character_name":"勇者","img_path":"images/hero.jpg"},
            {"character_id":75,"character_name":"バンカズ","img_path":"images/bankazu.jpg"},
            {"character_id":76,"character_name":"テリー","img_path":"images/terry.jpg"},
            {"character_id":77,"character_name":"ベレス","img_path":"images/byleth.jpg"},
            {"character_id":78,"character_name":"メンメン","img_path":"images/minmin.jpg"},
            {"character_id":79,"character_name":"スティーブ","img_path":"images/steve.jpg"},
            {"character_id":80,"character_name":"セフィロス","img_path":"images/sephiroth.jpg"},
            {"character_id":81,"character_name":"ホムヒカ","img_path":"images/homuhika.jpg"},
            {"character_id":82,"character_name":"カズヤ","img_path":"images/kazuya.jpg"},
            {"character_id":83,"character_name":"ソラ","img_path":"images/sora.jpg"},
            {"character_id":84,"character_name":"格闘mii","img_path":"images/mii_brawler.jpg"},
            {"character_id":85,"character_name":"剣術mii","img_path":"images/mii_sword.jpg"},
            {"character_id":86,"character_name":"射撃mii","img_path":"images/mii_gunner.jpg"},
        ]

        # for data in characters:
        #     character = Character(**data)
        #     character.save()
        print('成功')

        self.stdout.write(self.style.SUCCESS('this command Success'))