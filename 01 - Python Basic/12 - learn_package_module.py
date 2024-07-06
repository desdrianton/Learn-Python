import package_a as package_a                       # Cara 1 (Yang diimport keseluruhan package)
import package_a.module_a_1 as module_a_1           # Cara 2 (Yang diimport sebuah module)
from package_b import module_b_1                    # Cara 3

package_a.module_a_1.some_function_xxx1()
module_a_1.some_function_xxx2()
module_b_1.some_function_zzz1()
