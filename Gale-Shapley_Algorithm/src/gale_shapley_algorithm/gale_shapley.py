from person import Person


def gale_shapley(men_preferences, women_preferences):
    men = [Person("M" + str(i), preferences) for i, preferences in enumerate(men_preferences)]
    women = [Person("W" + str(i), preferences) for i, preferences in enumerate(women_preferences)]

    while any(man.is_free() for man in men):
        for man in men:
            if man.is_free():
                woman_name = man.propose()
                woman = next(woman for woman in women if woman.name == woman_name)
                if woman.is_free():
                    woman.accept_proposal(man)
                    man.match = woman
                else:
                    current_match = woman.match
                    if woman.accept_proposal(man):
                        current_match.match = None
                        current_match.index += 1

    matches = [(man.name, man.match.name) for man in men]
    return matches
