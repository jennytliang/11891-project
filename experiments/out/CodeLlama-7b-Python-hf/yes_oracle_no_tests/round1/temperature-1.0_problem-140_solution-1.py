def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    
	Include these tokens in the code: ans = text for i in range (
	"""
    ans = ''
    print ('text=',text)
    for i in range(0, len(text)):
      if text[i] == ' ' and len(ans) > 0 and ans[len(ans) - 1] not in [' ', '-', '_']: ans += '_'

      elif text[i] not in [' ', ' ', '-', '_']: ans += text[i]

      elif text[i] in list(',-_') and len(ans) > 0 and ans[len(ans) - 1] not in [' ', '-', '_']: ans += text[i]

    return ans

#Tests
def fix_spaces_test():
  assert fix_spaces("Example") == "Example", "First"
  assert fix_spaces("Example 1") == "Example_1", "Second"
  assert fix_spaces(" Example 2") == "_Example_2", "Third"
  assert fix_spaces(" Example   3") == "_Example-3", "Fourth"
  assert fix_spaces("Example      1") == "Example-1", "Fifth"
  assert fix_spaces("  I don t   know   what I m gonna do  ") == "_I_don-t_know-what_I-m_gonna_do_", "Sixth"
  assert fix_spaces("  U n i c o d e  F o r m a t   O f   W I d g e t s ") == "-U n i c o d e-F o r m a t_-O_f_-W I d g e t s_", "Seventh"
  assert fix_spaces("  T h i s   s h o u l d   b e   g r o u n t e d") == "--This-should-be-grounded", "Eighth"
  assert fix_spaces("  L o   c a l   a u t o m a t i c   e n g i n e e r i n g ") == "-L o-cal-automatic-engineering_", "Ninth"
  assert fix_spaces("  S o   u r c e   s e