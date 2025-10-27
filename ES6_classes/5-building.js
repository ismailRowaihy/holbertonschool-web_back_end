export default class Building{
    constructor(sqft){
        if (this.constructor === Building) {
             throw new Error("Class extending Building must override evacuationWarningMessage"); 
            }
        this._sqft=sqft;
    }
    get sqft(){
        return this._sqft;
    }
    set sqft(newSqft){
        this._sqft = newSqft
    }
    evacuationWarningMessage(){
        throw new Error('Class extending Building must override evacuationWarningMessage');
    }
}
