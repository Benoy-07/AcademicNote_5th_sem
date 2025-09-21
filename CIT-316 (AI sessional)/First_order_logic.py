# Rule: Gold(x) -> Glitters(x)

KB = {
    "Glitters": {"necklace", "ring", "silver", "platinum"},
    "Gold": {"ring", "gold", "goldennecklace"}
}

# Normalization helper
def norm(s: str) -> str:
    return s.strip().lower()

def glitters(x: str) -> bool:
    x = norm(x)
    # Gold implies Glitters
    return x in KB["Glitters"] or x in KB["Gold"]

def gold(x: str) -> bool:
    return norm(x) in KB["Gold"]

def add_fact(predicate: str, item: str):
    predicate = predicate.capitalize()
    item = norm(item)
    if predicate not in KB:
        KB[predicate] = set()
    KB[predicate].add(item)
    # maintain rule: if it's gold, also mark as glittering
    if predicate == "Gold":
        KB["Glitters"].add(item)

# ---- UI ----
print("Propositional Logic Form:  ∃x (Glitters(x) ∧ ¬Gold(x))")
print("Rule: Gold(x) -> Glitters(x)\n")

item = input("Enter a metal/item name: ").strip()
n = norm(item)
if not n:
    print("No input provided. Exiting.")
    raise SystemExit

if n not in KB["Glitters"] and n not in KB["Gold"]:
    print(f"\n{item.title()} is not in our knowledge base.")
    ans = input("Does it glitter? (yes/no): ").strip().lower()
    if ans.startswith("y"):
        add_fact("Glitters", n)
    ans = input("Is it gold? (yes/no): ").strip().lower()
    if ans.startswith("y"):
        add_fact("Gold", n)

# Per-item reasoning
print("\nResult for item:")
if glitters(n) and not gold(n):
    print(f"  {item.title()} glitters but is NOT gold. ✅ (Glitters(x) ∧ ¬Gold(x)) holds for this item.")
elif glitters(n) and gold(n):
    print(f"  {item.title()} glitters and IS gold.  (Gold implies Glitters.)")
else:
    print(f"  {item.title()} does not glitter in our knowledge base. ❌")

# Global check: does there exist any x s.t. Glitters(x) and not Gold(x)?
examples = sorted(x for x in KB["Glitters"] if x not in KB["Gold"])
print("\nGlobal check of the statement ∃x (Glitters(x) ∧ ¬Gold(x)):")
if examples:
    print(f"  TRUE — examples: {', '.join(e.title() for e in examples)}")
else:
    print("  FALSE — every glittering thing in KB is gold (no counterexample found).")
    
    
    
    
    
    