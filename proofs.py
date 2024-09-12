class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # Un diccionario para guardar los números que ya hemos visto
        for i, num in enumerate(nums):  # Recorremos la lista con sus índices
            complement = target - num  # Calculamos el número que falta para llegar al target
            if complement in seen:  # Si ese número que falta ya lo vimos antes
                return [seen[complement], i]  # Devolvemos los índices
            seen[num] = i  # Si no, guardamos el número actual en el diccionario

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Usamos un índice para realizar las operaciones en nums
        unique_index = 0

        # Diccionario para rastrear los elementos únicos
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = True
                nums[unique_index] = i
                unique_index += 1
        
        # Los elementos únicos están ahora al principio de nums
        return unique_index


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        flt = float(k)
        if len(nums) == k:
            return sum(nums)/k

        cut = len(nums) - k
        avrg = 0.0
        for i in range(len(nums) - cut):
            if (i + k) <= len(nums):
                if avrg < sum(nums[i:i+k])/flt:
                    avrg = sum(nums[i:i+k])/flt
        return avrg


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next  # Guardamos el siguiente nodo
            curr.next = prev       # Invertimos el puntero actual
            
            # Avanzamos los punteros
            prev = curr
            curr = next_node
        
        return prev  # Al final, prev será el nuevo head de la lista invertida


            

            