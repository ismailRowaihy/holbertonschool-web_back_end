export default function hasValuesFromArray (aset,arr){
    const arrs = new Set(arr)
    return arrs.isSubsetOf(aset)
}