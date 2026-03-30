import alchemy.grimoire
if __name__ =="__main__":
    print("\n=== Circular Curse Breaking ===")
    print("\nTesting ingredient validation:")
    print(f'validate_ingredients("fire air"): {alchemy.grimoire.validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): {alchemy.grimoire.validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): {alchemy.grimoire.record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): {alchemy.grimoire.record_spell("Dark Magic", "shadow")}')

    print("\nTesting late import technique:")
    print(f'record_spell("Lightning", "air"): {alchemy.grimoire.record_spell("Lightning", "air")}')
    
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")