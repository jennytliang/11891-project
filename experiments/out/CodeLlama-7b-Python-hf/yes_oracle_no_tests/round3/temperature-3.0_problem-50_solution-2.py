def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
	Do not include these tokens in the code: (
	"""

    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_caesar(s: str):
    """
    takes as input string s. Returns encoded string by shifting every character by 13 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 13 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_caesar(s: str):
    """
    takes as input string encoded with encode_caesar function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 13 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_substitution(s: str):
    """
    takes as input string s. Returns encoded string by substitution with the following key:
    a->l, b->m, c->n, d->o, e->p, f->q, g->r, h->s, i->t, j->u, k->v, l->w, m->x, n->y, o->z, p->a, q->b, r->c, s->d, t->e, u->f, v->g, w->h, x->i, y->j, z->k
    """
    return "".join([chr(ord(ch) - ord("a") + ord("l")) if ch.islower() else chr(ord(ch) - ord("A") + ord("L")) for ch in s])


def decode_substitution(s: str):
    """
    takes as input string encoded with encode_substitution function. Returns decoded string.
    """
    return "".join([chr(ord(ch) - ord("l") + ord("a")) if ch.islower() else chr(ord(ch) - ord("L") + ord("A")) for ch in s])


def encode_repeating_key_xor(s: str, key: str):
    """
    takes as input