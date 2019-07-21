-- State Monad:
type State' a = Integer -> (Integer,a)

unit :: a -> State' a
unit x y = (y,x)

bind :: State' a -> (a -> State' b) -> State' b
bind m f state = case m state of
  (state',r) -> f r state'

data StateM a = StateM (Integer -> (Integer,a))

instance Functor StateM where

instance Applicative StateM where

instance Monad StateM where
  return x = StateM (\state -> (state,x))
  (StateM m) >>= f = StateM (\state ->
     let
       (state',r ) = m state
       StateM g = f r
     in g state')

get :: StateM Integer
get = StateM $ \state -> (state,state)

put :: Integer -> StateM ()
put x = StateM $ \state -> (x,())

increment = do state <- get
               put (state + 1)

run :: StateM a -> Integer
run (StateM m) = fst (m 0)

{-
--Simplification of increment

  increment
  = get >>= \state -> put (state + 1)                               -- expand definition of `increment`
  = (StateM (\s -> (s,s)) >>= (\cur -> put (cur + 1))               -- expand definition of `get`
  = StateM (\state ->                                               -- expand >>= definition
     let
       (state',r ) = (\s -> (s,s)) state
       StateM g = (\cur -> put (cur + 1)) r
     in g state')
  = StateM (\state ->                                               -- beta reduce (two places)
     let
       (state',r) = (state,state)
       StateM g = put (r + 1)
     in g state')
  = StateM (\state ->                                               -- reduce first let binding
     let
       StateM g = put (state + 1)
     in g state)
  = StateM (\state ->                                               -- expand `put`
     let
       StateM g = (\x -> StateM $ \_ -> (x,())) (state + 1)
     in g state)
  = StateM (\state ->                                               -- beta reduce
     let
       StateM g = StateM (\_ -> (state + 1,()))
     in g state
  = StateM (\state -> (\_ -> (state + 1,())) state                  -- reduce let
  = StateM (\state -> (state + 1,()))                               -- beta reduce

run increment
= run (StateM (\state -> (state + 1,())))                           -- expand `increment` with above
= fst ((\state -> (state + 1,())) 0)                                -- expand `run`
= fst (0 + 1,())                                                    -- beta reduce
= 0 + 1                                                             -- reduce `fst`
= 1

-}


--each :: [IO a] -> IO [a]
each [] = return []
each (x:xs) = do y <- x
                 ys <- each xs
                 return (y:ys)

{-
while :: Monad m => (m Bool) -> m () -> m ()
while c m = do b <- c
               if b then m >> while c m else return ()
-}

fact' n k = if n == 0
            then k 1
            else fact' (n-1) (\t -> k (n*t))

{-
-- derivation that `fact' 2 (\x -> x)` really is 2.

fact' 2 (\x -> x)
  = if 2 == 0 then (\x -> x) 2 else fact' (2 - 1) (\t -> (\x -> x) (2*t))
  = fact' (2 - 1) (\t -> (\x -> x) (2*t))
  = fact' 1 (\t -> (2*t))
  = if 1 == 0 then (\t -> (2*t)) 2 else fact' (1 - 1) (\s -> (\t -> (2*t)) (1*s))
  = fact' 0 (\s -> (\t -> (2*t)) (1*s))
  = if 0 == 0 then (\s -> (\t -> (2*t)) (1*s)) 1 else (0-1) (\r -> (\s -> (\t -> (2*t)) (1*s)) (0*r))
  = (\s -> (\t -> (2*t)) (1*s)) 1
  = (\t -> (2*t)) (1*1)
  = 2*(1*1)
  = 2*1
  = 2
-}

{-
  d = a -> e
  e = b -> f
  f = c -> g
  h = bool
  j = m
  j = g
  i = c -> h
  a = b -> i
  k = c -> j
  a = int -> k
  l = string -> m
  a = b -> l

  d = (int -> string -> bool) -> int -> (string -> bool)
-}