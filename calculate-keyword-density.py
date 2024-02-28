import re
from collections import Counter

def calculate_keyword_density(text, keywords):
    # Remove special characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    words = cleaned_text.split()
    total_words = len(words)

    # Count the occurrences of each keyword
    keyword_counts = Counter(words)
    keyword_density = {}

    for keyword in keywords:
        count = keyword_counts.get(keyword, 0)
        density = (count / total_words) * 100
        keyword_density[keyword] = density

    return keyword_density

# Example usage
blog_post = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vulputate sagittis purus eget tincidunt. Ut finibus, purus et viverra tristique, ante dui aliquet purus, a lobortis justo nunc non mauris. Vestibulum eu metus at justo iaculis interdum. Aliquam id varius lacus. Duis et justo turpis. Cras accumsan ligula mi, non porttitor ex efficitur nec. Sed pellentesque felis ut justo aliquet bibendum. Curabitur et magna id neque semper auctor nec quis ligula. Nunc posuere volutpat augue, ut tempus tellus venenatis id. Sed convallis arcu sed libero auctor, vel pulvinar velit laoreet. Vestibulum lacinia dapibus bibendum. Etiam a risus ac ipsum sollicitudin accumsan. Suspendisse et tincidunt massa, eu dignissim turpis.

Vestibulum eget ante eget justo interdum rutrum. Ut interdum nisi vitae lorem ullamcorper, vitae ullamcorper odio vehicula. Integer euismod nulla nec nunc posuere fermentum. Suspendisse egestas finibus facilisis. Maecenas facilisis laoreet aliquam. Nulla faucibus pulvinar tincidunt. Mauris vel arcu sit amet elit pellentesque pellentesque. Suspendisse aliquet diam ac fermentum tristique. Phasellus sit amet justo ut nunc bibendum ullamcorper nec et sapien. Integer rhoncus, neque non vulputate placerat, lacus elit faucibus enim, eget faucibus odio nulla eu lacus. Nunc id justo non est vestibulum vestibulum. Etiam vehicula consequat velit nec eleifend.

Sed volutpat tristique enim, id vulputate sem consequat vitae. Sed efficitur turpis sed odio dapibus, in eleifend velit eleifend. Aliquam at viverra nunc. Nulla non leo vitae ex bibendum consectetur eu eu tellus. Suspendisse potenti. Proin tristique varius lacus ut consequat. Pellentesque viverra purus leo, vitae venenatis ligula efficitur et. In vestibulum maximus neque, vel fringilla erat interdum ac. Fusce suscipit metus eget tellus pulvinar, sit amet volutpat ipsum scelerisque. Sed vitae diam auctor, efficitur lorem sed, vestibulum elit. Cras vel congue sem. Suspendisse sit amet ultrices justo, id dapibus odio.

Aliquam laoreet nisi felis, at tempor dolor bibendum eget. Morbi eleifend turpis id erat pellentesque scelerisque. Ut dapibus enim eu lobortis volutpat. Maecenas varius ex ac urna consequat lobortis. Nulla sollicitudin venenatis justo, a egestas risus consectetur et. Nam non rutrum neque, at aliquam urna. Nullam ac blandit sapien. In gravida eleifend mi. Sed congue enim a turpis congue posuere. Proin tincidunt, nisl sed tincidunt lobortis, est quam condimentum est, ac posuere risus enim vel lacus. Maecenas dapibus risus enim, et condimentum sem pulvinar sed. Nullam varius sagittis nisi id sagittis. Suspendisse eget mauris tellus. In dapibus velit ut mi efficitur, at euismod velit rutrum. Nunc id varius sem.

Donec sit amet lectus purus. Nulla eget cursus lacus. Donec et sapien consectetur, vulputate nunc vitae, semper enim. Sed rutrum feugiat ipsum, id volutpat mauris. Morbi iaculis urna et enim efficitur facilisis. Quisque pulvinar lacus non orci gravida aliquet. Integer a nunc eget odio viverra finibus sed vel dui. Integer sodales venenatis tellus et iaculis. Ut iaculis metus vel fringilla interdum. Vestibulum tempor fringilla diam eget feugiat. Vestibulum commodo metus sit amet felis varius, et gravida felis viverra. Curabitur a ex eget erat suscipit consequat. Suspendisse ac ligula sit amet justo placerat consectetur.

Etiam varius, elit et tincidunt cursus, metus enim pulvinar arcu, ut sollicitudin ligula sem vitae purus. Nam dapibus, est in facilisis rutrum, orci sem ultrices neque, non egestas tellus turpis eu nibh. Donec sit amet mi ipsum. Duis eget nulla vitae elit aliquam mattis id in ipsum. Aenean laoreet enim non odio ultrices, vitae fringilla ante viverra. Maecenas posuere eros at sem sagittis consequat. Ut semper, neque eget efficitur fringilla, diam nisl viverra mi, ac tempus lacus mi id neque. Sed mattis lorem et ultrices ullamcorper. Nullam vestibulum semper ligula, vel sollicitudin mauris dapibus vel. Nam lobortis facilisis feugiat. In nec mauris orci. Maecenas ultrices massa eget dui condimentum commodo.
"""

target_keywords = ['SEO', 'keyword', 'density', 'blog']

keyword_density = calculate_keyword_density(blog_post, target_keywords)

# Print the keyword density
for keyword, density in keyword_density.items():
    print(f"Keyword: {keyword}, Density: {density:.2f}%")
