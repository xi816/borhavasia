import sys;

CONSONANTS = "бвгћджзѕјкѯлмнпѱрстуфѳхцчш";
VOWELS = "аиоуїӓӧӱ";

def main(s: str):
  s = s.lower();
  if (s[0] == "г"):
    s = "ћ"+s[1:];
  s = s.replace("е", "ѣ");
  s = s.replace("тс", "ц");
  s = s.replace("цк", "с");
  s = s.replace("кс", "ѯ");
  s = s.replace("пс", "ѱ");
  s = s.replace("э", "є");
  s = s.replace("дж", "ѕ");
  s = s.replace("дз", "ѕ");
  s = s.replace("ль", "л̀");
  s = s.replace("нь", "н̀");
  s = s.replace("ий", "ѵ");
  s = s.replace("ш", "х");
  s = s.replace("ия", "іо");
  s = s.replace("у", "оу̀");
  s = s.replace("я", "ӓ");
  s = s.replace("ё", "ӧ");
  s = s.replace("ю", "ӱ");
  s = s.replace("ы", "ї");
  s = s.replace("ин", "іу̀");
  if ((len(s) > 1) and ((s[-2:] in ["л̀", "н̀"]) or (s[-1] in CONSONANTS))):
    s += "ъ";
  s = list(s);
  for i in enumerate(s):
    if ((i[1] == "и") and (i[0] != len(s)-1) and (s[i[0]+1] in VOWELS)):
      s[i[0]] = "і";
  return "".join(s);

s = sys.argv[1];

if (not s.count("-")):
  print(main(sys.argv[1]));
else:
  for i in enumerate(s.split("-")):
    print(main(i[1]), end="");
    if (i[0] != len(s.split("-"))-1):
      print("-", end="");
  print();

