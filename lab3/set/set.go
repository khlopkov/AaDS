package set

type Set struct{
	set [] int
}

func NewSet(n int) *Set{
	set := Set{
		set: make([]int, n),
	}
	for i:=0; i<n; i++{
		set.set[i] = i
	}
	return &set
}
func (set *Set) Get(v int) int{
	if v == set.set[v]{
		return v
	} else {
		set.set[v] = set.Get(set.set[v])
		return set.set[v]
	}
}
func (set *Set) Unite(a int, b int){
	a = set.Get(a)
	b = set.Get(b)
	if (a != b){
		set.set[a] = b;
	}
}