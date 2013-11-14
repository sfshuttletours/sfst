import logging,os
import shelve,pickle
###############################################################################

log = logging.getLogger('shelf.py')

class Shelf:
   """
      Leightweight persistant storage
   """
   def __init__(self, fname=None, create=True):
      self.is_open=False
      self.fname = fname or self.generateFilename()
      self.open(fname=self.fname,create=create)

   def open(self,create=True,fname=None): 
      fname = fname or self.fname
      if not create: 
         err = 'create is set to True but path@'+self.fname+' does not exist'
         assert os.path.exists(self.fname),err
         self.shelf = shelve.open(self.fname)
      else:
         if not os.path.exists(self.fname):
            self.shelf = shelve.open(self.fname)
         else: self.shelf = shelve.open(self.fname)
      log.debug('shelf@'+self.fname+' opened')
      self.is_open=True
   def unset(self,k): 
         if isinstance(k,unicode): k=str(k)
         if k in self.keys(): del self.shelf[k]
         self.sync()
         
   def generateFilename(self):
      fname = os.path.join(os.getcwd(),self.__class__.__name__+'.db')
      return fname
   def values(self): return self.shelf.values()
   def keys(self): self.sync(); self.close(); self.open(); return self.shelf.keys()
   def items(self):
	return [[k,self.grab(k)] for k in self.keys()]
   def grab(self,k):
      if isinstance(k,int) or isinstance(k,unicode): k=str(k)
      if k in self.keys():
	      try: v = self.shelf[k]
	      except KeyError: return None
	      return pickle.loads(v)
   
      
   def sync(self): 
      self.shelf.sync();# self.shelf.close(); self.shelf = shelve.open(self.fname)
   save=sync
   def append(self,k,d):
      lst = self.grab(k)
      if lst==None: lst=[]
      assert isinstance(lst,list),'dunno how to append for nonlist'
      lst.append(d)
      self.put(k,lst)

   def put(self,k,d):
      """
      """
      if isinstance(k,int):      k = str(k)
      if isinstance(k,unicode):  k = str(k)
      self.shelf[k] = pickle.dumps(d);
      self.shelf.sync()

   def close(self):     
      ret=self.shelf.close()
      self.is_open=False
      return ret
   def Print(self):
      for k in self.shelf.keys(): print self.grab(k)
   def __setitem__(self,k,v): return self.put(k,v)
   def __getitem__(self,k):   return self.grab(k)

def test():
   class ShelfSub(Shelf): pass
   s = ShelfSub()
   print s.fname
   s.Print()
   s.put('a',{'a':'b'})
   s.close()

if __name__=='__main__':
   import sys
   if len(sys.argv)==2:
      fname = sys.argv[-1]
      s = Shelf(fname=fname)
      s.Print()
   else:
      test()