from itertools import product
import jdqd.a04.relation.relation_pt.algor.relation_util
from jdqd.a04.relation.relation_pt.algor import pattern

base_words = ['尽管', '虽然', '固然']
contrast_words = ['但是', '然而', '可是', '但', '还是', '却']
keywords = list(product(base_words, contrast_words))
keywords_single = [[w] for w in contrast_words]

keyword_rules = {
    'rule101': keywords,
    'rule102': keywords,
    'rule103': keywords,
    'rule104': keywords,
    'rule201': keywords_single,
    'rule202': keywords_single,
    'rule301': keywords,
    'rule302': keywords,
    'rule4': keywords
}

def rule101(sentence, keyword):
    # 匹配模式: ...虽然..., ...但是...
    return pattern.rule_skcscskcs(sentence, keyword)


def rule102(sentence, keyword):
    # 匹配模式: ...虽然..., 但是...
    return pattern.rule_skscks(sentence, keyword)


def rule103(sentence, keyword):
    # 匹配模式: 虽然..., ...但是...
    return pattern.rule_kscsks(sentence, keyword)


def rule104(sentence, keyword):
    # 匹配模式: 虽然..., 但是...
    return pattern.rule_kscks(sentence, keyword)


def rule201(sentence, keyword):
    # 匹配模式: ..., ...但是...
    return pattern.rule_scsks(sentence, keyword)


def rule202(sentence, keyword):
    # 匹配模式: ..., 但是...
    return pattern.rule_sckcs(sentence, keyword, comma2=False)


def rule301(sentence, keyword):
    # 匹配模式: ...虽然..., ...
    return pattern.rule_skcscs(sentence, keyword)


def rule302(sentence, keyword):
    # 匹配模式: 虽然..., ...
    return pattern.rule_kscs(sentence, keyword)


def rule4(sentence, keyword):
    # 匹配模式: ..., 虽然...
    return pattern.rule_sckcs(sentence, keyword, reverse=True, comma2=False)


rules = [rule101, rule102, rule103, rule201, rule202, rule301, rule302, rule4]
keyword_rules = relation_util.tuple_to_list(keyword_rules)

