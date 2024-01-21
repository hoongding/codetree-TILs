const main = () => {
    const firstCompare = b > a && b > c;
    const secondCompare = b === a && b === c;
    
    return `${firstCompare} ${secondCompare}`;
}