from sentimentja import Analyzer
from pprint import pprint

analyzer = Analyzer(version=1)
pprint(analyzer.analyze(["ファイナル・ファンタジーは楽しい", "クソゲーはつまらん"]))
