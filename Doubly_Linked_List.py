
class DoublyList:
  
    def __init__(self, a):

        if type(a)==list:
            self.head = Node(a[0],None,None)
            tail=self.head

            for i in range(1,len(a)):
                Newnode=Node(a[i],None,None)
                z=tail
                tail.next=Newnode
                
                tail=Newnode
                tail.prev=z
        else:
            self.head=a
        
     
    def countNode(self):

        n=self.head
        count=0

        while n!=None:
            count+=1
            n=n.next

        return count
    
    
    def forwardprint(self):
        n=self.head
        
        while n!=None:

            if n.next==None:
                print(n.element)
            else:
                print(n.element,end=",")
                
            n=n.next
    
    
    def backwardprint(self):

        n=self.head
        count=self.countNode()

        while n.next!=None:
            n=n.next
        
    
        while n!=None:
            if count==1:
                print(n.element)
            else:
                print(n.element,end=",")

            count-=1
            n=n.prev
    
    def nodeAt(self, idx):
        if idx<0 or idx>=self.countNode():
            return None

        n=self.head
        i=0

        while n!=None:
            if i==idx:
                return n
        
            n=n.next
      
            i+=1
    
    # returns the index of the containing the given element. if the element does not exist in the List, return -1.
    def indexOf(self, elem):

        n=self.head
        i=0

        while n!=None:
            if n.element==elem:
                z=i
        
                return z
            n=n.next
      
            i+=1
        return -1

    
    def insert(self, elem, idx):
        if idx<0 or idx>self.countNode():
            return None

        if idx==0:

            newnode=Node(elem,None,None)
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode

        elif idx==self.countNode():

            newnode=Node(elem,None,None)
            pred=self.nodeAt(idx-1)
            newnode.prev=pred
            pred.next=newnode

        else:
            
            newnode=Node(elem,None,None)
            pred=self.nodeAt(idx-1)
            suc=self.nodeAt(idx)

            suc.prev=newnode
            newnode.prev=pred
            pred.next=newnode

            newnode.next=suc


    def remove(self, idx):
	if idx<0 or idx>=self.countNode():
            return None

        z=self.nodeAt(idx).element        

      	if idx==0:
            n=self.head
            
            self.head=n.next
            self.head.prev=None
            n.next=None
            n.element=None

        elif idx==self.countNode()-1:

            rem=self.nodeAt(idx)
            pred=self.nodeAt(idx-1)
            pred.next=None

            rem.element=None
            rem.next=Node
            rem.prev=None

        else:
            rem=self.nodeAt(idx)
            pred=self.nodeAt(idx-1)
            suc=self.nodeAt(idx+1)

            pred.next=suc
            suc.prev=pred
            rem.next=None

            rem.prev=None
            rem.element=None

        return str(z)
